from django.db import models

class Paste(models.Model):
	id = models.CharField(max_length=8, primary_key=True)
	title = models.CharField(max_length=60, blank=True,
		help_text='Optional title for this paste')

	creation_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title or 'Untitled'

	class Meta:
		ordering = ['-creation_date']

class PasteFile(models.Model):
	id = models.CharField(max_length=36, primary_key=True)
	name = models.CharField(max_length=60, blank=True,
		help_text='Optional name for this file')
	contents = models.CharField(max_length=1024*512, blank=True)
	language = models.CharField(max_length=20,
		help_text='Language, used for syntax highlighting, etc.')

	paste = models.ForeignKey(Paste, related_name='files')

	def __str__(self):
		return self.name or 'Untitled'

	class Meta:
		ordering = ['paste']
