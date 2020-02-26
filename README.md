## 起動
### 前提条件
 - DockerおよびDocker Composeがシステムへインストールされていること。
 - 

```
git clone { event_info_api }
docker-compose up -d
docker-compose exec api bash
python manage.py migrate
```
