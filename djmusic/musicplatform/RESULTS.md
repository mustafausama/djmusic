# Steps taken in populating djMusic database

## Importing models

We first need to import the models from their respective modules

```python
from albums.models import Album
from artists.models import Artist
```

## Creating sample Artists and Albums

We then create two sample artists with stage names: **Cassandra** and **Asphodel** (with an empty social link)

```python
cassandra = Artist(
  stage_name='Cassandra',
  social_link='https://www.instagram.com/cassandra/'
  )

asphodel = Artist(
  stage_name='Asphodel',
  social_link=''
  )

cassandra.save()
asphodel.save()
```

We apply queries for listing down the artists as required:

- List down all artists

  ```python
  >>> Artist.objects.all()

  <QuerySet [<Artist: Asphodel>, <Artist: Cassandra>]>
  ```

- List down all artists sorted by name

  ```python
  >>> Artist.objects.order_by('stage_name')

  <QuerySet [<Artist: Asphodel>, <Artist: Cassandra>]>
  ```

- List down all artists whose name starts with `a` _Notice **a** is different from **A**_

  ```python
  >>> Artist.objects.filter(stage_name__startswith='a')
  <QuerySet []>

  >>> Artist.objects.filter(stage_name__startswith='A')
  <QuerySet [<Artist: Asphodel>]>
  ```

We also, after importing datetime libraries, create 3 sample albums associated with the created artists:

- **On the road** (Cassandra), with creation and release dates in the past
- **Along the Way** (Cassandra), with creation date in the past and release date as today
- **By the Seaside** (Asphodel), with creation date as today and release date in the future

Here, two different ways are used to create the albums and associate them with the artists

```python
import datetime
from django.utils import timezone

on_the_road = Album(
  artist=cassandra,
  album_name='On the road',
  created_at = timezone.now() - datetime.timedelta(days=15),
  released_at = timezone.now() - datetime.timedelta(days=10),
  cost=39.95
  )

on_the_road.save()

along_the_way = cassandra.album_set.create(
  artist=cassandra,
  album_name='Along the Way',
  created_at = timezone.now() - datetime.timedelta(days=5),
  released_at = timezone.now(),

  cost=59.99
  )

by_the_seaside = Album(
  artist=asphodel,
  album_name='By the Seaside',
  released_at=timezone.now() + datetime.timedelta(days=5),
  cost=99.99
  )

by_the_seaside.save()
```

We apply queries for listing down the albums as required:

- Get the latest released album

  > Because there might be albums with **future release date**, we need to, first, **chop them off**, then, **sort** the remaining **descendingly** by **release date**.

  ```python
  >>> Album.objects.filter(released_at__lte=timezone.now()).order_by('-released_at')[0]

  <Album: Along the Way>
  ```

- Get all albums released before today

  ```python
  >>> today_start = timezone.localtime(timezone.now()).replace(hour=0, minute=0, second=0, microsecond=0)
  >>> Album.objects.filter(released_at__lt=today_start)

  <QuerySet [<Album: On the road>]>
  ```

- Get all albums released today or before but not after today

  ```python
  >>> next_day_start = timezone.localtime(timezone.now()+datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
  >>> Album.objects.filter(released_at__lt=next_day_start)

  <QuerySet [<Album: On the road>, <Album: Along the Way>]>
  ```

- Count the total number of albums

  ```python
  >>> Album.objects.count()
  3
  ```

- In 2 different ways, for each artist, list down all of his/her albums

  ```python
  >>> from django.db.models import Count
  >>> Album.objects.values('artist').annotate(album_count=Count('id'))
  <QuerySet [{'artist': 1, 'album_count': 2}, {'artist': 2, 'album_count': 1}]>

  >>> [
  ...   {
  ...     'artist': artist.id,
  ...     'album_count': artist.album_set.count()
  ...   }
  ...   for artist in Artist.objects.all()
  ... ]
  [{'artist': 2, 'album_count': 1}, {'artist': 1, 'album_count': 2}]
  ```

- List down all albums ordered by cost then by name
  ```python
  >>> Album.objects.order_by('cost', 'album_name')
  <QuerySet [<Album: On the road>, <Album: Along the Way>, <Album: By the Seaside>]>
  ```
