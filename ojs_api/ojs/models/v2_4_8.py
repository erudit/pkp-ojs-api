# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import json

from django.db import models

from .v2_4_8_extra import *  # noqa


DATABASE = 'ojs'


class Journals(models.Model):
    _DATABASE = DATABASE

    journal_id = models.BigIntegerField(
        primary_key=True,
        help_text="""Automatic OJS instance internal id.
        """)
    path = models.CharField(
        unique=True,
        max_length=32,
        help_text="""Journal unique identifier.
        A short word or acronym that identifies the journal. Used in URL.
        """
    )
    seq = models.FloatField(
        help_text="""Automatic field.
        Not managed via admin interface.
        """
    )
    primary_locale = models.CharField(
        max_length=5,
        help_text="""Form Language.
        """
    )
    enabled = models.IntegerField(
        help_text="""Enable this journal to appear publicly on the site.
        """
    )

    def settings(self, locale=None, name=None):
        """Returns the setting(s) of this Journal for a specific locale.

        If no locale provided, uses the default locale (provided in the
        'Form Language' in the admin interface).

        If no name provided, returns all the settings.

        Settings returned are a list of tuples : (name, value, type)
        """
        if locale is None:
            locale = self.primary_locale

        if name is None:
            results = JournalSettings.objects.filter(
                journal_id=self.journal_id,
                locale=locale,
            )
        else:
            results = JournalSettings.objects.filter(
                journal_id=self.journal_id,
                locale=locale,
                name=name,
            )
        settings = []
        for r in results:
            settings.append(
                (r.setting_name, r.setting_value, r.setting_type)
            )
        return settings

    def title(self, locale=None):
        """Returns the name of this Journal for a specific locale.
        If no locale provided, uses the default locale (provided in the
        'Form Language' in the admin interface).
        """
        name, value, type = self.settings(locale, name='title')[0]
        return value

    def description(self, locale=None):
        """Returns the description of this Journal for a specific locale.
        If no locale provided, uses the default locale (provided in the
        'Form Language' in the admin interface).
        """
        name, value, type = self.settings(locale, name='description')[0]
        return value

    def __str__(self):
        return "{} [{}]".format(
            self.path,
            self.journal_id,
        )

    class Meta:
        managed = False
        db_table = 'journals'


class JournalSettings(models.Model):
    """Settings for a Journal set for a specific locale.

    Here's the settings for Journals (excluding system settings)

    Journal
    * title
    * description

    Languages
    * supportedFormLocales
    * supportedLocales
    * supportedSubmissionLocales

    System
    * ...
    """
    _DATABASE = DATABASE

    journal_id = models.ForeignKey(
        'Journals',
        to_field='journal_id',  # should'nt be necessary
        help_text="""Journal identifier.
        Contributes to multiple primary key.
        """,
        db_column='journal_id',
    )
    locale = models.CharField(
        max_length=5,
        help_text="""Language of the settings.
        Contributes to multiple primary key.
        """,
    )
    setting_name = models.CharField(
        max_length=255,
        help_text="""Name (key) of the setting.
        Contributes to multiple primary key.
        """,
    )
    setting_value = models.TextField(
        blank=True,
        null=True,
        help_text="""Value of the setting.
        """,
    )
    setting_type = models.CharField(
        max_length=6,
        help_text="""Type of the setting.
        """,
    )

    class Meta:
        managed = False
        db_table = 'journal_settings'
        unique_together = (('journal_id', 'locale', 'setting_name'),)


class Issues(models.Model):
    _DATABASE = DATABASE

    issue_id = models.BigIntegerField(primary_key=True)
    journal_id = models.ForeignKey(
        'Journals',
        related_name='issues',
    )
    volume = models.SmallIntegerField(blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    published = models.IntegerField()
    current = models.IntegerField()
    date_published = models.DateTimeField(blank=True, null=True)
    date_notified = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    access_status = models.IntegerField()
    open_access_date = models.DateTimeField(blank=True, null=True)
    show_volume = models.IntegerField()
    show_number = models.IntegerField()
    show_year = models.IntegerField()
    show_title = models.IntegerField()
    style_file_name = models.CharField(max_length=90, blank=True, null=True)
    original_style_file_name = models.CharField(max_length=255, blank=True, null=True)

    def settings(self, locale=None, name=None):
        """Returns the setting(s) of this Issue for a specific locale.

        If no locale provided, uses the default locale of the Journal
        (provided in the 'Form Language' in the admin interface).

        If no name provided, returns all the settings.

        Settings returned are a list of tuples : (name, value, type)
        """
        if locale is None:
            locale = self.journal_id.primary_locale

        if name is None:
            results = IssueSettings.objects.filter(
                issue_id=self.issue_id,
                locale=locale,
            )
        else:
            results = IssueSettings.objects.filter(
                issue_id=self.issue_id,
                locale=locale,
                name=name,
            )
        settings = []
        for r in results:
            settings.append(
                (r.setting_name, r.setting_value, r.setting_type)
            )
        return settings

    def title(self, locale=None):
        """Returns the name of this Issue for a specific locale.
        If no locale provided, uses the default locale of the Journal
        (provided in the 'Form Language' in the admin interface).
        """
        name, value, type = self.settings(locale, name='title')[0]
        return value

    def description(self, locale=None):
        """Returns the description of this Issue for a specific locale.
        If no locale provided, uses the default locale of the Journal
        (provided in the 'Form Language' in the admin interface).
        """
        name, value, type = self.settings(locale, name='description')[0]
        return value

    def __str__(self):
        return "{} [{}]".format(
            self.issue_id,
            self.issue_id,
        )
    class Meta:
        managed = False
        db_table = 'issues'


class IssueFiles(models.Model):
    _DATABASE = DATABASE

    file_id = models.BigIntegerField(primary_key=True)
    issue_id = models.BigIntegerField()
    file_name = models.CharField(max_length=90)
    file_type = models.CharField(max_length=255)
    file_size = models.BigIntegerField()
    content_type = models.BigIntegerField()
    original_file_name = models.CharField(max_length=127, blank=True, null=True)
    date_uploaded = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'issue_files'


class IssueSettings(models.Model):
    """Settings of an Issue set for a specific locale.

    Issue
    * title
    * description

    Cover (Allowed formats: .gif, .jpg, or .png)
    * fileName
    * originalFileName
    * height
    * width
    * coverPageAltText
    * coverPageDescription
    * hideCoverPageArchives
    * hideCoverPageCover
    * showCoverPage
    """
    _DATABASE = DATABASE

    issue_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'issue_settings'
        unique_together = (('issue_id', 'locale', 'setting_name'),)


class Articles(models.Model):
    _DATABASE = DATABASE

    article_id = models.BigIntegerField(primary_key=True)
    locale = models.CharField(max_length=5, blank=True, null=True)
    user_id = models.BigIntegerField()
    journal_id = models.BigIntegerField()
    section_id = models.BigIntegerField(blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    comments_to_ed = models.TextField(blank=True, null=True)
    citations = models.TextField(blank=True, null=True)
    date_submitted = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    date_status_modified = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    submission_progress = models.IntegerField()
    current_round = models.IntegerField()
    submission_file_id = models.BigIntegerField(blank=True, null=True)
    revised_file_id = models.BigIntegerField(blank=True, null=True)
    review_file_id = models.BigIntegerField(blank=True, null=True)
    editor_file_id = models.BigIntegerField(blank=True, null=True)
    pages = models.CharField(max_length=255, blank=True, null=True)
    fast_tracked = models.IntegerField()
    hide_author = models.IntegerField()
    comments_status = models.IntegerField()

    def to_json(self):
        return json.dumps(self)

    def from_json(self, data):
        json_data = json.loads(data)
        for k, v in json_data.items():
            #self.date_submitted =
            pass

    class Meta:
        managed = False
        db_table = 'articles'


class ArticleFiles(models.Model):
    _DATABASE = DATABASE

    file_id = models.BigIntegerField()
    revision = models.BigIntegerField()
    source_file_id = models.BigIntegerField(blank=True, null=True)
    source_revision = models.BigIntegerField(blank=True, null=True)
    article_id = models.BigIntegerField()
    file_name = models.CharField(max_length=90)
    file_type = models.CharField(max_length=255)
    file_size = models.BigIntegerField()
    original_file_name = models.CharField(max_length=127, blank=True, null=True)
    file_stage = models.BigIntegerField()
    viewable = models.IntegerField(blank=True, null=True)
    date_uploaded = models.DateTimeField()
    date_modified = models.DateTimeField()
    round = models.IntegerField()
    assoc_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_files'
        unique_together = (('file_id', 'revision'),)


class ArticleSettings(models.Model):
    _DATABASE = DATABASE

    article_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'article_settings'
        unique_together = (('article_id', 'locale', 'setting_name'),)


class ArticleSuppFileSettings(models.Model):
    _DATABASE = DATABASE

    supp_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'article_supp_file_settings'
        unique_together = (('supp_id', 'locale', 'setting_name'),)


class ArticleSupplementaryFiles(models.Model):
    _DATABASE = DATABASE

    supp_id = models.BigIntegerField(primary_key=True)
    file_id = models.BigIntegerField()
    article_id = models.BigIntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    remote_url = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    show_reviewers = models.IntegerField(blank=True, null=True)
    date_submitted = models.DateTimeField()
    seq = models.FloatField()

    class Meta:
        managed = False
        db_table = 'article_supplementary_files'
