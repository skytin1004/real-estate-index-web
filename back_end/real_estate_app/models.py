from django.db import models

# 뉴스 조회
class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title

# 정부 이슈 조회
class Issue(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title

# 지역 조회 (서울, 경기, 인천, 부산, 대구, 광주, 대전, 울산, 세종, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주)
class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 지역별 구 조회(서울: 강남구, 강동구, 강북구, 강서구, 관악구, 광진구, 구로구, 금천구, 노원구, 도봉구, 동대문구, 동작구, 마포구, 서대문구, 서초구, 성동구, 성북구, 송파구, 양천구, 영등포구, 용산구, 은평구, 종로구, 중구, 중랑구)
class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, related_name='districts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name