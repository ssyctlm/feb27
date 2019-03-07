# How to rename app in Django

![96](https://cdn2.jianshu.io/assets/default_avatar/4-3397163ecdb3855a0a4139c34a695885.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96)

 

[ccphantom](https://www.jianshu.com/u/369ec73f4b8e)

 

关注

2017.09.09 05:05* 字数 271 阅读 171评论 0喜欢 0

Follow these steps to change an app's name in Django:

1. Rename the folder which is in your project root
2. Change any references to your app in their dependencies, i.e. the app's `views.py`, `urls.py` , `'manage.py'`, and `settings.py` files.
3. Edit the database table `django_content_type` with the following command:

```
UPDATE django_content_type SET app_label='<NewAppName>' 
WHERE app_label='<OldAppName>'
```

1. Also if you have models, you will have to rename the model tables. For postgres use

```
ALTER TABLE <oldAppName>_modelName 
RENAME TO <newAppName>_modelName.
```

1. (For Django >= 1.7) Update the django_migrations table to avoid having your previous migrations re-run:

```
UPDATE django_migrations SET app='<NewAppName>'
WHERE app='<OldAppName>'. 
```

**Note: there is some debate (in comments) if this step is required for Django 1.8+; If someone knows for sure please update here.**

1. If your `models.py's` Meta Class has `app_name` listed, make sure to rename that too .
2. If you've namespaced your `static` or `templates` folders inside your app, you'll also need to rename those. For example, rename `old_app/static/old_app` to `new_app/static/new_app`.
3. For renaming Django models, you'll need to change django_content_type.model entry in DB. For PostgreSQL use

```
UPDATE django_content_type SET model='<newModelName>' 
where model='<oldModelName>' AND app_label='<OldAppName>'
```

1. if you're using the new migrations, you'll need to change the app name in the **existing migrations files** (such as **dependency module names**) and `django_migrations` table. It might be better to squash migrations first so there's less to edit.
2. For Postgres, If you want to rename the sequence too, then use

```
ALTER SEQUENCE <oldAppName>_<modelName>_<PK>_seq 
RENAME TO <newAppName>_<modelName>_<PK>_seq 
```

Although it is not necessary, the system itself doesn't care about the name. The column DEFAULT stores an OID ('foo_pkey_seq'::regclass), you can change the name of the sequence without breaking that - the OID stays the same.