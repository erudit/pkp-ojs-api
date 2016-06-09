# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccessKeys(models.Model):
    access_key_id = models.BigIntegerField(primary_key=True)
    context = models.CharField(max_length=40)
    key_hash = models.CharField(max_length=40)
    user_id = models.BigIntegerField()
    assoc_id = models.BigIntegerField(blank=True, null=True)
    expiry_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'access_keys'


class AnnouncementSettings(models.Model):
    announcement_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'announcement_settings'
        unique_together = (('announcement_id', 'locale', 'setting_name'),)


class AnnouncementTypeSettings(models.Model):
    type_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'announcement_type_settings'
        unique_together = (('type_id', 'locale', 'setting_name'),)


class AnnouncementTypes(models.Model):
    type_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.SmallIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'announcement_types'


class Announcements(models.Model):
    announcement_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.SmallIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField()
    type_id = models.BigIntegerField(blank=True, null=True)
    date_expire = models.DateTimeField(blank=True, null=True)
    date_posted = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'announcements'


class ArticleComments(models.Model):
    comment_id = models.BigIntegerField(primary_key=True)
    comment_type = models.BigIntegerField(blank=True, null=True)
    role_id = models.BigIntegerField()
    article_id = models.BigIntegerField()
    assoc_id = models.BigIntegerField()
    author_id = models.BigIntegerField()
    comment_title = models.CharField(max_length=255)
    comments = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    viewable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_comments'


class ArticleGalleySettings(models.Model):
    galley_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'article_galley_settings'
        unique_together = (('galley_id', 'locale', 'setting_name'),)


class ArticleGalleys(models.Model):
    galley_id = models.BigIntegerField(primary_key=True)
    locale = models.CharField(max_length=5, blank=True, null=True)
    article_id = models.BigIntegerField()
    file_id = models.BigIntegerField()
    label = models.CharField(max_length=32, blank=True, null=True)
    html_galley = models.IntegerField()
    style_file_id = models.BigIntegerField(blank=True, null=True)
    seq = models.FloatField()
    remote_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_galleys'


class ArticleHtmlGalleyImages(models.Model):
    galley_id = models.BigIntegerField()
    file_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'article_html_galley_images'
        unique_together = (('galley_id', 'file_id'),)


class ArticleSearchKeywordList(models.Model):
    keyword_id = models.BigIntegerField(primary_key=True)
    keyword_text = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'article_search_keyword_list'


class ArticleSearchObjectKeywords(models.Model):
    object_id = models.BigIntegerField()
    keyword_id = models.BigIntegerField()
    pos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'article_search_object_keywords'
        unique_together = (('object_id', 'pos'),)


class ArticleSearchObjects(models.Model):
    object_id = models.BigIntegerField(primary_key=True)
    article_id = models.BigIntegerField()
    type = models.IntegerField()
    assoc_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_search_objects'


class ArticleXmlGalleys(models.Model):
    xml_galley_id = models.BigIntegerField(primary_key=True)
    galley_id = models.BigIntegerField()
    article_id = models.BigIntegerField()
    label = models.CharField(max_length=32)
    galley_type = models.CharField(max_length=255)
    views = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'article_xml_galleys'


class AuthSources(models.Model):
    auth_id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    plugin = models.CharField(max_length=32)
    auth_default = models.IntegerField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_sources'


class AuthorSettings(models.Model):
    author_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'author_settings'
        unique_together = (('author_id', 'locale', 'setting_name'),)


class Authors(models.Model):
    author_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField()
    primary_contact = models.IntegerField()
    seq = models.FloatField()
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=90)
    suffix = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=90, blank=True, null=True)
    email = models.CharField(max_length=90)
    url = models.CharField(max_length=255, blank=True, null=True)
    user_group_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authors'


class BooksForReview(models.Model):
    book_id = models.BigIntegerField(primary_key=True)
    journal_id = models.BigIntegerField()
    status = models.SmallIntegerField()
    author_type = models.SmallIntegerField()
    publisher = models.CharField(max_length=255)
    year = models.SmallIntegerField()
    language = models.CharField(max_length=10)
    copy = models.IntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    edition = models.IntegerField(blank=True, null=True)
    pages = models.SmallIntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=30, blank=True, null=True)
    date_created = models.DateTimeField()
    date_requested = models.DateTimeField(blank=True, null=True)
    date_assigned = models.DateTimeField(blank=True, null=True)
    date_mailed = models.DateTimeField(blank=True, null=True)
    date_due = models.DateTimeField(blank=True, null=True)
    date_submitted = models.DateTimeField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    editor_id = models.BigIntegerField(blank=True, null=True)
    article_id = models.BigIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books_for_review'


class BooksForReviewAuthors(models.Model):
    author_id = models.BigIntegerField(primary_key=True)
    book_id = models.BigIntegerField()
    seq = models.FloatField()
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=90)

    class Meta:
        managed = False
        db_table = 'books_for_review_authors'


class BooksForReviewSettings(models.Model):
    book_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'books_for_review_settings'
        unique_together = (('book_id', 'locale', 'setting_name'),)


class Captchas(models.Model):
    captcha_id = models.BigIntegerField(primary_key=True)
    session_id = models.CharField(max_length=40)
    value = models.CharField(max_length=20)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'captchas'


class CitationSettings(models.Model):
    citation_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'citation_settings'
        unique_together = (('citation_id', 'locale', 'setting_name'),)


class Citations(models.Model):
    citation_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()
    citation_state = models.BigIntegerField()
    raw_citation = models.TextField(blank=True, null=True)
    seq = models.BigIntegerField()
    lock_id = models.CharField(max_length=23, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citations'
        unique_together = (('assoc_type', 'assoc_id', 'seq'),)


class Comments(models.Model):
    comment_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField()
    parent_comment_id = models.BigIntegerField(blank=True, null=True)
    num_children = models.IntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)
    poster_ip = models.CharField(max_length=15)
    poster_name = models.CharField(max_length=90, blank=True, null=True)
    poster_email = models.CharField(max_length=90, blank=True, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class CompletedPayments(models.Model):
    completed_payment_id = models.BigIntegerField(primary_key=True)
    timestamp = models.DateTimeField()
    payment_type = models.BigIntegerField()
    journal_id = models.BigIntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    amount = models.FloatField()
    currency_code_alpha = models.CharField(max_length=3, blank=True, null=True)
    payment_method_plugin_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'completed_payments'


class ControlledVocabEntries(models.Model):
    controlled_vocab_entry_id = models.BigIntegerField(primary_key=True)
    controlled_vocab_id = models.BigIntegerField()
    seq = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'controlled_vocab_entries'


class ControlledVocabEntrySettings(models.Model):
    controlled_vocab_entry_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'controlled_vocab_entry_settings'
        unique_together = (('controlled_vocab_entry_id', 'locale', 'setting_name'),)


class ControlledVocabs(models.Model):
    controlled_vocab_id = models.BigIntegerField(primary_key=True)
    symbolic = models.CharField(max_length=64)
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'controlled_vocabs'
        unique_together = (('symbolic', 'assoc_type', 'assoc_id'),)


class CustomIssueOrders(models.Model):
    issue_id = models.BigIntegerField(unique=True)
    journal_id = models.BigIntegerField()
    seq = models.FloatField()

    class Meta:
        managed = False
        db_table = 'custom_issue_orders'


class CustomSectionOrders(models.Model):
    issue_id = models.BigIntegerField()
    section_id = models.BigIntegerField()
    seq = models.FloatField()

    class Meta:
        managed = False
        db_table = 'custom_section_orders'
        unique_together = (('issue_id', 'section_id'),)


class DataObjectTombstoneOaiSetObjects(models.Model):
    object_id = models.BigIntegerField(primary_key=True)
    tombstone_id = models.BigIntegerField()
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'data_object_tombstone_oai_set_objects'


class DataObjectTombstoneSettings(models.Model):
    tombstone_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'data_object_tombstone_settings'
        unique_together = (('tombstone_id', 'locale', 'setting_name'),)


class DataObjectTombstones(models.Model):
    tombstone_id = models.BigIntegerField(primary_key=True)
    data_object_id = models.BigIntegerField()
    date_deleted = models.DateTimeField()
    set_spec = models.CharField(max_length=255)
    set_name = models.CharField(max_length=255)
    oai_identifier = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'data_object_tombstones'


class DataverseFiles(models.Model):
    dvfile_id = models.BigIntegerField(primary_key=True)
    supp_id = models.BigIntegerField()
    submission_id = models.BigIntegerField()
    study_id = models.BigIntegerField()
    content_source_uri = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'dataverse_files'


class DataverseStudies(models.Model):
    study_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField()
    edit_uri = models.CharField(max_length=255)
    edit_media_uri = models.CharField(max_length=255)
    statement_uri = models.CharField(max_length=255)
    persistent_uri = models.CharField(max_length=255)
    data_citation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataverse_studies'


class EditAssignments(models.Model):
    edit_id = models.BigIntegerField(primary_key=True)
    article_id = models.BigIntegerField()
    editor_id = models.BigIntegerField()
    can_edit = models.IntegerField()
    can_review = models.IntegerField()
    date_assigned = models.DateTimeField(blank=True, null=True)
    date_notified = models.DateTimeField(blank=True, null=True)
    date_underway = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edit_assignments'


class EditDecisions(models.Model):
    edit_decision_id = models.BigIntegerField(primary_key=True)
    article_id = models.BigIntegerField()
    round = models.IntegerField()
    editor_id = models.BigIntegerField()
    decision = models.IntegerField()
    date_decided = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'edit_decisions'


class EmailLog(models.Model):
    log_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    sender_id = models.BigIntegerField()
    date_sent = models.DateTimeField()
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    event_type = models.BigIntegerField(blank=True, null=True)
    from_address = models.CharField(max_length=255, blank=True, null=True)
    recipients = models.TextField(blank=True, null=True)
    cc_recipients = models.TextField(blank=True, null=True)
    bcc_recipients = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_log'


class EmailLogUsers(models.Model):
    email_log_id = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'email_log_users'
        unique_together = (('email_log_id', 'user_id'),)


class EmailTemplates(models.Model):
    email_id = models.BigIntegerField(primary_key=True)
    email_key = models.CharField(max_length=64)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'email_templates'
        unique_together = (('email_key', 'assoc_type', 'assoc_id'),)


class EmailTemplatesData(models.Model):
    email_key = models.CharField(max_length=64)
    locale = models.CharField(max_length=5)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    subject = models.CharField(max_length=120)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_templates_data'
        unique_together = (('email_key', 'locale', 'assoc_type', 'assoc_id'),)


class EmailTemplatesDefault(models.Model):
    email_id = models.BigIntegerField(primary_key=True)
    email_key = models.CharField(max_length=64)
    can_disable = models.IntegerField()
    can_edit = models.IntegerField()
    from_role_id = models.BigIntegerField(blank=True, null=True)
    to_role_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_templates_default'


class EmailTemplatesDefaultData(models.Model):
    email_key = models.CharField(max_length=64)
    locale = models.CharField(max_length=5)
    subject = models.CharField(max_length=120)
    body = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_templates_default_data'
        unique_together = (('email_key', 'locale'),)


class EventLog(models.Model):
    log_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    date_logged = models.DateTimeField()
    ip_address = models.CharField(max_length=39)
    event_type = models.BigIntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    is_translated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_log'


class EventLogSettings(models.Model):
    log_id = models.BigIntegerField()
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'event_log_settings'
        unique_together = (('log_id', 'setting_name'),)


class ExternalFeedSettings(models.Model):
    feed_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'external_feed_settings'
        unique_together = (('feed_id', 'locale', 'setting_name'),)


class ExternalFeeds(models.Model):
    feed_id = models.BigIntegerField(primary_key=True)
    journal_id = models.BigIntegerField()
    url = models.CharField(max_length=255)
    seq = models.FloatField()
    display_homepage = models.IntegerField()
    display_block = models.SmallIntegerField()
    limit_items = models.IntegerField(blank=True, null=True)
    recent_items = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_feeds'


class FilterGroups(models.Model):
    filter_group_id = models.BigIntegerField(primary_key=True)
    symbolic = models.CharField(unique=True, max_length=255, blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    input_type = models.CharField(max_length=255, blank=True, null=True)
    output_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filter_groups'


class FilterSettings(models.Model):
    filter_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'filter_settings'
        unique_together = (('filter_id', 'locale', 'setting_name'),)


class Filters(models.Model):
    filter_id = models.BigIntegerField(primary_key=True)
    filter_group_id = models.BigIntegerField()
    context_id = models.BigIntegerField()
    display_name = models.CharField(max_length=255, blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    is_template = models.IntegerField()
    parent_filter_id = models.BigIntegerField()
    seq = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'filters'


class Gifts(models.Model):
    gift_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.SmallIntegerField()
    assoc_id = models.BigIntegerField()
    status = models.IntegerField()
    gift_type = models.SmallIntegerField()
    gift_assoc_id = models.BigIntegerField()
    buyer_first_name = models.CharField(max_length=40)
    buyer_middle_name = models.CharField(max_length=40, blank=True, null=True)
    buyer_last_name = models.CharField(max_length=90)
    buyer_email = models.CharField(max_length=90)
    buyer_user_id = models.BigIntegerField(blank=True, null=True)
    recipient_first_name = models.CharField(max_length=40)
    recipient_middle_name = models.CharField(max_length=40, blank=True, null=True)
    recipient_last_name = models.CharField(max_length=90)
    recipient_email = models.CharField(max_length=90)
    recipient_user_id = models.BigIntegerField(blank=True, null=True)
    date_redeemed = models.DateTimeField(blank=True, null=True)
    locale = models.CharField(max_length=5)
    gift_note_title = models.CharField(max_length=90, blank=True, null=True)
    gift_note = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gifts'


class GroupMemberships(models.Model):
    user_id = models.BigIntegerField()
    group_id = models.BigIntegerField()
    about_displayed = models.IntegerField()
    seq = models.FloatField()

    class Meta:
        managed = False
        db_table = 'group_memberships'
        unique_together = (('user_id', 'group_id'),)


class GroupSettings(models.Model):
    group_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'group_settings'
        unique_together = (('group_id', 'locale', 'setting_name'),)


class Groups(models.Model):
    group_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.SmallIntegerField(blank=True, null=True)
    publish_email = models.SmallIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    context = models.BigIntegerField(blank=True, null=True)
    about_displayed = models.IntegerField()
    seq = models.FloatField()

    class Meta:
        managed = False
        db_table = 'groups'


class InstitutionalSubscriptionIp(models.Model):
    institutional_subscription_ip_id = models.BigIntegerField(primary_key=True)
    subscription_id = models.BigIntegerField()
    ip_string = models.CharField(max_length=40)
    ip_start = models.BigIntegerField()
    ip_end = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institutional_subscription_ip'


class InstitutionalSubscriptions(models.Model):
    institutional_subscription_id = models.BigIntegerField(primary_key=True)
    subscription_id = models.BigIntegerField()
    institution_name = models.CharField(max_length=255)
    mailing_address = models.CharField(max_length=255, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institutional_subscriptions'




class IssueGalleySettings(models.Model):
    galley_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'issue_galley_settings'
        unique_together = (('galley_id', 'locale', 'setting_name'),)


class IssueGalleys(models.Model):
    galley_id = models.BigIntegerField(primary_key=True)
    locale = models.CharField(max_length=5, blank=True, null=True)
    issue_id = models.BigIntegerField()
    file_id = models.BigIntegerField()
    label = models.CharField(max_length=32, blank=True, null=True)
    seq = models.FloatField()

    class Meta:
        managed = False
        db_table = 'issue_galleys'


class MetadataDescriptionSettings(models.Model):
    metadata_description_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'metadata_description_settings'
        unique_together = (('metadata_description_id', 'locale', 'setting_name'),)


class MetadataDescriptions(models.Model):
    metadata_description_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()
    schema_namespace = models.CharField(max_length=255)
    schema_name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    seq = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'metadata_descriptions'


class Metrics(models.Model):
    load_id = models.CharField(max_length=255)
    assoc_type = models.BigIntegerField()
    context_id = models.BigIntegerField()
    issue_id = models.BigIntegerField(blank=True, null=True)
    submission_id = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField()
    day = models.CharField(max_length=8, blank=True, null=True)
    month = models.CharField(max_length=6, blank=True, null=True)
    file_type = models.IntegerField(blank=True, null=True)
    country_id = models.CharField(max_length=2, blank=True, null=True)
    region = models.CharField(max_length=2, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    metric_type = models.CharField(max_length=255)
    metric = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metrics'


class Mutex(models.Model):
    i = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'mutex'


class Notes(models.Model):
    note_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    file_id = models.BigIntegerField(blank=True, null=True)
    contents = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notes'


class NotificationMailList(models.Model):
    notification_mail_list_id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=90)
    confirmed = models.IntegerField()
    token = models.CharField(max_length=40)
    context = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'notification_mail_list'
        unique_together = (('email', 'context'),)


class NotificationSettings(models.Model):
    notification_id = models.BigIntegerField()
    locale = models.CharField(max_length=5, blank=True, null=True)
    setting_name = models.CharField(max_length=64)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'notification_settings'
        unique_together = (('notification_id', 'locale', 'setting_name'),)


class NotificationSubscriptionSettings(models.Model):
    setting_id = models.BigIntegerField(primary_key=True)
    setting_name = models.CharField(max_length=64)
    setting_value = models.TextField(blank=True, null=True)
    user_id = models.BigIntegerField()
    context = models.BigIntegerField()
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'notification_subscription_settings'


class Notifications(models.Model):
    notification_id = models.BigIntegerField(primary_key=True)
    context_id = models.BigIntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)
    level = models.BigIntegerField()
    type = models.BigIntegerField()
    date_created = models.DateTimeField()
    date_read = models.DateTimeField(blank=True, null=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class OaiResumptionTokens(models.Model):
    token = models.CharField(unique=True, max_length=32)
    expire = models.BigIntegerField()
    record_offset = models.IntegerField()
    params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oai_resumption_tokens'


class ObjectForReviewAssignments(models.Model):
    assignment_id = models.BigIntegerField(primary_key=True)
    object_id = models.BigIntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)
    submission_id = models.BigIntegerField(blank=True, null=True)
    status = models.SmallIntegerField()
    date_requested = models.DateTimeField(blank=True, null=True)
    date_assigned = models.DateTimeField(blank=True, null=True)
    date_mailed = models.DateTimeField(blank=True, null=True)
    date_due = models.DateTimeField(blank=True, null=True)
    date_reminded_before = models.DateTimeField(blank=True, null=True)
    date_reminded_after = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'object_for_review_assignments'
        unique_together = (('object_id', 'user_id'),)


class ObjectForReviewPersons(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    object_id = models.BigIntegerField()
    seq = models.FloatField()
    role = models.CharField(max_length=255)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=90)

    class Meta:
        managed = False
        db_table = 'object_for_review_persons'


class ObjectForReviewSettings(models.Model):
    object_id = models.BigIntegerField()
    review_object_metadata_id = models.BigIntegerField()
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'object_for_review_settings'
        unique_together = (('object_id', 'review_object_metadata_id'),)


class ObjectsForReview(models.Model):
    object_id = models.BigIntegerField(primary_key=True)
    review_object_type_id = models.BigIntegerField()
    context_id = models.BigIntegerField()
    available = models.IntegerField()
    date_created = models.DateTimeField()
    editor_id = models.BigIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objects_for_review'


class PaypalTransactions(models.Model):
    txn_id = models.CharField(primary_key=True, max_length=17)
    txn_type = models.CharField(max_length=20, blank=True, null=True)
    payer_email = models.CharField(max_length=127, blank=True, null=True)
    receiver_email = models.CharField(max_length=127, blank=True, null=True)
    item_number = models.CharField(max_length=127, blank=True, null=True)
    payment_date = models.CharField(max_length=127, blank=True, null=True)
    payer_id = models.CharField(max_length=13, blank=True, null=True)
    receiver_id = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paypal_transactions'


class PlnDepositObjects(models.Model):
    deposit_object_id = models.BigIntegerField(primary_key=True)
    journal_id = models.BigIntegerField()
    object_id = models.BigIntegerField()
    object_type = models.CharField(max_length=36)
    deposit_id = models.BigIntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pln_deposit_objects'


class PlnDeposits(models.Model):
    deposit_id = models.BigIntegerField(primary_key=True)
    journal_id = models.BigIntegerField()
    uuid = models.CharField(max_length=36, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    date_status = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pln_deposits'


class PluginSettings(models.Model):
    plugin_name = models.CharField(max_length=80)
    locale = models.CharField(max_length=5)
    journal_id = models.BigIntegerField()
    setting_name = models.CharField(max_length=80)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'plugin_settings'
        unique_together = (('plugin_name', 'locale', 'journal_id', 'setting_name'),)


class Processes(models.Model):
    process_id = models.CharField(unique=True, max_length=23)
    process_type = models.IntegerField()
    time_started = models.BigIntegerField()
    obliterated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'processes'


class PublishedArticles(models.Model):
    published_article_id = models.BigIntegerField(primary_key=True)
    article_id = models.BigIntegerField(unique=True)
    issue_id = models.BigIntegerField()
    date_published = models.DateTimeField(blank=True, null=True)
    seq = models.FloatField()
    access_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'published_articles'


class QueuedPayments(models.Model):
    queued_payment_id = models.BigIntegerField(primary_key=True)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    expiry_date = models.DateField(blank=True, null=True)
    payment_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queued_payments'


class ReferralSettings(models.Model):
    referral_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'referral_settings'
        unique_together = (('referral_id', 'locale', 'setting_name'),)


class Referrals(models.Model):
    referral_id = models.BigIntegerField(primary_key=True)
    article_id = models.BigIntegerField()
    status = models.SmallIntegerField()
    url = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    link_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'referrals'
        unique_together = (('article_id', 'url'),)


class ReviewAssignments(models.Model):
    review_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField()
    reviewer_id = models.BigIntegerField()
    competing_interests = models.TextField(blank=True, null=True)
    regret_message = models.TextField(blank=True, null=True)
    recommendation = models.IntegerField(blank=True, null=True)
    date_assigned = models.DateTimeField(blank=True, null=True)
    date_notified = models.DateTimeField(blank=True, null=True)
    date_confirmed = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    date_acknowledged = models.DateTimeField(blank=True, null=True)
    date_due = models.DateTimeField(blank=True, null=True)
    date_response_due = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    reminder_was_automatic = models.IntegerField()
    declined = models.IntegerField()
    replaced = models.IntegerField()
    cancelled = models.IntegerField()
    reviewer_file_id = models.BigIntegerField(blank=True, null=True)
    date_rated = models.DateTimeField(blank=True, null=True)
    date_reminded = models.DateTimeField(blank=True, null=True)
    quality = models.IntegerField(blank=True, null=True)
    review_round_id = models.BigIntegerField(blank=True, null=True)
    stage_id = models.IntegerField()
    review_method = models.IntegerField()
    round = models.IntegerField()
    step = models.IntegerField()
    review_form_id = models.BigIntegerField(blank=True, null=True)
    unconsidered = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_assignments'


class ReviewFormElementSettings(models.Model):
    review_form_element_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'review_form_element_settings'
        unique_together = (('review_form_element_id', 'locale', 'setting_name'),)


class ReviewFormElements(models.Model):
    review_form_element_id = models.BigIntegerField(primary_key=True)
    review_form_id = models.BigIntegerField()
    seq = models.FloatField(blank=True, null=True)
    element_type = models.BigIntegerField(blank=True, null=True)
    required = models.IntegerField(blank=True, null=True)
    included = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_form_elements'


class ReviewFormResponses(models.Model):
    review_form_element_id = models.BigIntegerField()
    review_id = models.BigIntegerField()
    response_type = models.CharField(max_length=6, blank=True, null=True)
    response_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_form_responses'


class ReviewFormSettings(models.Model):
    review_form_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'review_form_settings'
        unique_together = (('review_form_id', 'locale', 'setting_name'),)


class ReviewForms(models.Model):
    review_form_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    seq = models.FloatField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_forms'


class ReviewObjectMetadata(models.Model):
    metadata_id = models.BigIntegerField(primary_key=True)
    review_object_type_id = models.BigIntegerField()
    seq = models.FloatField(blank=True, null=True)
    metadata_type = models.BigIntegerField(blank=True, null=True)
    required = models.IntegerField(blank=True, null=True)
    display = models.IntegerField(blank=True, null=True)
    metadata_key = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_object_metadata'


class ReviewObjectMetadataSettings(models.Model):
    metadata_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'review_object_metadata_settings'
        unique_together = (('metadata_id', 'locale', 'setting_name'),)


class ReviewObjectTypeSettings(models.Model):
    type_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'review_object_type_settings'
        unique_together = (('type_id', 'locale', 'setting_name'),)


class ReviewObjectTypes(models.Model):
    type_id = models.BigIntegerField(primary_key=True)
    context_id = models.BigIntegerField()
    is_active = models.IntegerField()
    type_key = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_object_types'


class ReviewRounds(models.Model):
    review_round_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField()
    stage_id = models.BigIntegerField(blank=True, null=True)
    round = models.IntegerField()
    review_revision = models.BigIntegerField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_rounds'
        unique_together = (('submission_id', 'stage_id', 'round'),)


class Roles(models.Model):
    journal_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    role_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'roles'
        unique_together = (('journal_id', 'user_id', 'role_id'),)


class RtContexts(models.Model):
    context_id = models.BigIntegerField(primary_key=True)
    version_id = models.BigIntegerField()
    title = models.CharField(max_length=120)
    abbrev = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    cited_by = models.IntegerField()
    author_terms = models.IntegerField()
    define_terms = models.IntegerField()
    geo_terms = models.IntegerField()
    seq = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rt_contexts'


class RtSearches(models.Model):
    search_id = models.BigIntegerField(primary_key=True)
    context_id = models.BigIntegerField()
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    search_url = models.TextField(blank=True, null=True)
    search_post = models.TextField(blank=True, null=True)
    seq = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rt_searches'


class RtVersions(models.Model):
    version_id = models.BigIntegerField(primary_key=True)
    journal_id = models.BigIntegerField()
    version_key = models.CharField(max_length=40)
    locale = models.CharField(max_length=5, blank=True, null=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rt_versions'


class ScheduledTasks(models.Model):
    class_name = models.CharField(unique=True, max_length=255)
    last_run = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scheduled_tasks'


class SectionEditors(models.Model):
    journal_id = models.BigIntegerField()
    section_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    can_edit = models.IntegerField()
    can_review = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'section_editors'
        unique_together = (('journal_id', 'section_id', 'user_id'),)


class SectionSettings(models.Model):
    section_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'section_settings'
        unique_together = (('section_id', 'locale', 'setting_name'),)


class Sections(models.Model):
    section_id = models.BigIntegerField(primary_key=True)
    journal_id = models.BigIntegerField()
    review_form_id = models.BigIntegerField(blank=True, null=True)
    seq = models.FloatField()
    editor_restricted = models.IntegerField()
    meta_indexed = models.IntegerField()
    meta_reviewed = models.IntegerField()
    abstracts_not_required = models.IntegerField()
    hide_title = models.IntegerField()
    hide_author = models.IntegerField()
    hide_about = models.IntegerField()
    disable_comments = models.IntegerField()
    abstract_word_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sections'


class Sessions(models.Model):
    session_id = models.CharField(unique=True, max_length=128)
    user_id = models.BigIntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=39)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    created = models.BigIntegerField()
    last_used = models.BigIntegerField()
    remember = models.IntegerField()
    data = models.TextField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'


class Signoffs(models.Model):
    signoff_id = models.BigIntegerField(primary_key=True)
    symbolic = models.CharField(max_length=32)
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    file_id = models.BigIntegerField(blank=True, null=True)
    file_revision = models.BigIntegerField(blank=True, null=True)
    date_notified = models.DateTimeField(blank=True, null=True)
    date_underway = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    date_acknowledged = models.DateTimeField(blank=True, null=True)
    user_group_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'signoffs'
        unique_together = (('assoc_type', 'assoc_id', 'symbolic', 'user_id', 'user_group_id', 'file_id', 'file_revision'),)


class Site(models.Model):
    redirect = models.BigIntegerField()
    primary_locale = models.CharField(max_length=5)
    min_password_length = models.IntegerField()
    installed_locales = models.CharField(max_length=255)
    supported_locales = models.CharField(max_length=255, blank=True, null=True)
    original_style_file_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site'


class SiteSettings(models.Model):
    setting_name = models.CharField(max_length=255)
    locale = models.CharField(max_length=5)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'site_settings'
        unique_together = (('setting_name', 'locale'),)


class StaticPageSettings(models.Model):
    static_page_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'static_page_settings'
        unique_together = (('static_page_id', 'locale', 'setting_name'),)


class StaticPages(models.Model):
    static_page_id = models.BigIntegerField(primary_key=True)
    path = models.CharField(max_length=255)
    journal_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'static_pages'


class SubscriptionTypeSettings(models.Model):
    type_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'subscription_type_settings'
        unique_together = (('type_id', 'locale', 'setting_name'),)


class SubscriptionTypes(models.Model):
    type_id = models.BigIntegerField(primary_key=True)
    journal_id = models.BigIntegerField()
    cost = models.FloatField()
    currency_code_alpha = models.CharField(max_length=3)
    non_expiring = models.IntegerField()
    duration = models.SmallIntegerField(blank=True, null=True)
    format = models.SmallIntegerField()
    institutional = models.IntegerField()
    membership = models.IntegerField()
    disable_public_display = models.IntegerField()
    seq = models.FloatField()

    class Meta:
        managed = False
        db_table = 'subscription_types'


class Subscriptions(models.Model):
    subscription_id = models.BigIntegerField(primary_key=True)
    journal_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    type_id = models.BigIntegerField()
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    date_reminded_before = models.DateTimeField(blank=True, null=True)
    date_reminded_after = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    membership = models.CharField(max_length=40, blank=True, null=True)
    reference_number = models.CharField(max_length=40, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriptions'


class TemporaryFiles(models.Model):
    file_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    file_name = models.CharField(max_length=90)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    file_size = models.BigIntegerField()
    original_file_name = models.CharField(max_length=127, blank=True, null=True)
    date_uploaded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'temporary_files'


class Theses(models.Model):
    thesis_id = models.BigIntegerField(primary_key=True)
    journal_id = models.BigIntegerField()
    status = models.SmallIntegerField()
    degree = models.SmallIntegerField()
    degree_name = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    date_approved = models.DateTimeField()
    title = models.CharField(max_length=255)
    url = models.TextField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    student_first_name = models.CharField(max_length=40)
    student_middle_name = models.CharField(max_length=40, blank=True, null=True)
    student_last_name = models.CharField(max_length=90)
    student_email = models.CharField(max_length=90)
    student_email_publish = models.IntegerField(blank=True, null=True)
    student_bio = models.TextField(blank=True, null=True)
    supervisor_first_name = models.CharField(max_length=40)
    supervisor_middle_name = models.CharField(max_length=40, blank=True, null=True)
    supervisor_last_name = models.CharField(max_length=90)
    supervisor_email = models.CharField(max_length=90)
    discipline = models.CharField(max_length=255, blank=True, null=True)
    subject_class = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    coverage_geo = models.CharField(max_length=255, blank=True, null=True)
    coverage_chron = models.CharField(max_length=255, blank=True, null=True)
    coverage_sample = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    date_submitted = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'theses'


class UsageStatsTemporaryRecords(models.Model):
    assoc_id = models.BigIntegerField()
    assoc_type = models.BigIntegerField()
    day = models.BigIntegerField()
    metric = models.BigIntegerField()
    country_id = models.CharField(max_length=2, blank=True, null=True)
    region = models.CharField(max_length=2, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    load_id = models.CharField(max_length=255)
    file_type = models.IntegerField(blank=True, null=True)
    entry_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'usage_stats_temporary_records'


class UserInterests(models.Model):
    user_id = models.BigIntegerField()
    controlled_vocab_entry_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_interests'
        unique_together = (('user_id', 'controlled_vocab_entry_id'),)


class UserSettings(models.Model):
    user_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'user_settings'
        unique_together = (('user_id', 'locale', 'setting_name', 'assoc_type', 'assoc_id'),)


class Users(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=32)
    password = models.CharField(max_length=255)
    salutation = models.CharField(max_length=40, blank=True, null=True)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=90)
    suffix = models.CharField(max_length=40, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    initials = models.CharField(max_length=5, blank=True, null=True)
    email = models.CharField(unique=True, max_length=90)
    url = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    mailing_address = models.CharField(max_length=255, blank=True, null=True)
    billing_address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=90, blank=True, null=True)
    locales = models.CharField(max_length=255, blank=True, null=True)
    date_last_email = models.DateTimeField(blank=True, null=True)
    date_registered = models.DateTimeField()
    date_validated = models.DateTimeField(blank=True, null=True)
    date_last_login = models.DateTimeField()
    must_change_password = models.IntegerField(blank=True, null=True)
    auth_id = models.BigIntegerField(blank=True, null=True)
    auth_str = models.CharField(max_length=255, blank=True, null=True)
    disabled = models.IntegerField()
    disabled_reason = models.TextField(blank=True, null=True)
    inline_help = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Versions(models.Model):
    major = models.IntegerField()
    minor = models.IntegerField()
    revision = models.IntegerField()
    build = models.IntegerField()
    date_installed = models.DateTimeField()
    current = models.IntegerField()
    product_type = models.CharField(max_length=30, blank=True, null=True)
    product = models.CharField(max_length=30, blank=True, null=True)
    product_class_name = models.CharField(max_length=80, blank=True, null=True)
    lazy_load = models.IntegerField()
    sitewide = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'versions'
        unique_together = (('product_type', 'product', 'major', 'minor', 'revision', 'build'),)
