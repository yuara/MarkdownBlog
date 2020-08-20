from django.db import models
import markdown

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def markdown_to_html(self):
        """
        Convert markdown to html and create an index.
        """

        # extra: an extar function for codeblocks and tables
        # admonition: can use for warning messages
        # sane_lists: can make lists
        # toc: create an index automatically
        md = markdown.Markdown(extensions=["extra", "admonition", "sane_lists", "toc"])
        html = md.convert(self.content)
        return html

        # No extra function for strikethrough so you have to use the del tag.
