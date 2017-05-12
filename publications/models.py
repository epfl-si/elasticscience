from django.db import models

from .search import PublicationIndex


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Publication(models.Model):
    title = models.CharField(max_length=200)
    doi = models.CharField(max_length=200)
    pub_date = models.DateField()
    authors = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def indexing(self):
        """
        Creates the object used by ES to index.
        """
        obj = PublicationIndex(
            meta={'id': self.id},
            title=self.title,
            doi=self.doi,
            pub_date=self.pub_date,
            authors=self.authors
        )

        obj.save(index='publications')  # Saves the object to ES.

        return obj.to_dict(include_meta=True)
