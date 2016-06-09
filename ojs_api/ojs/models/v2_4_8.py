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

    journal_id = models.BigIntegerField(primary_key=True)
    path = models.CharField(unique=True, max_length=32)
    seq = models.FloatField()
    primary_locale = models.CharField(max_length=5)
    enabled = models.IntegerField()

    def __str__(self):
        return "{} [{}]".format(
            self.path,
            self.journal_id,
        )

    class Meta:
        managed = False
        db_table = 'journals'


class JournalSettings(models.Model):
    _DATABASE = DATABASE

    journal_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'journal_settings'
        unique_together = (('journal_id', 'locale', 'setting_name'),)


class Issues(models.Model):
    _DATABASE = DATABASE

    issue_id = models.BigIntegerField(primary_key=True)
    journal_id = models.BigIntegerField()
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
            self.date_submitted =

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
