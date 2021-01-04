<p align="center">
  <img src="https://github.com/lnxpy/codehub/blob/master/git_components/gitbanner.png" width="550px">
  <br>
  <br>
  <b>کد هاب</b>
  <br>
  <span>سرویس پیست بین پارسی</span>
  <br>
  <a href="https://github.com/lnxpy/codehub/blob/master/README_fa.md">پارسی</a> ◆
  <a href="https://github.com/lnxpy/codehub/blob/master/README.md">English</a>
  </p>

<h2 dir="rtl" align="right">کد هاب</h2>
<p dir="rtl" align="right">
 کد هاب یک پلتفورم برای آرشیو کردن خطا ها، ایرادات و اسکریپت هایی هست که قصد دارید با دیگران به اشتراک بذارید. نمونه کد هاب رو ممکنه خیلی جاها دیده باشید اما این پلتفورم کاملا فارسی، رایگان و همچنین قابل دسترس برای تمامی دوستان هست.
</p>
<p dir="rtl" align="right">
در کد هاب نه تنها میتونید مشکلات برنامه نویسی خودتون رو به اشتراک بذارید، بلکه به راحتی میتونید اسکریپت های کارساز و ماژول ها رو به صورت دستی بنویسید و در شبکه های اجتماعی برای دوستانتون ارسال کنید.
  </p>

<h2 dir="rtl" align="right">Api</h2>
<p dir="rtl" align="right">
  خدمات CodeHub API ارائه شده اند تا این سرویس در هر پلتفرم و دستگاهی که استفاده می کنید انعطاف پذیرتر و قابل دسترسی تر باشد. راه های متعددی برای ساخت یک اسنیپت یا باز کردن هر یک از آن ها وجود دارد. شما می توانید از سرویس های API استفاده کنید تا یک CodeHub کوچک بر روی سیستم محلی خود داشته باشد بدون هیچ وابستگی.
</p>

<h2 dir="rtl" align="right">1. GET</h2>
<p dir="rtl" align="right">
  تمام اطلاعات مربوط به یک اسنیپت را دریافت کنید. شما نیاز به دانستن SnippetIdentification (SID) بنابراین شما می توانید تمام داده ها را از پایگاه داده بخوانید.
</p>

```
POINT: http://codehub.pythonanywhere.com/api/vX/snippet/<SID>

RESULT
{
    "SID": "##########",
    "title": "TITLE",
    "detail": "DETAILS",
    "script": "SCRIPT",
    "error": "ERROR",
    "language": "python",
    "pub_date": "۶ فروردین ۱۳۹۹",
    "link": "http://codehub.pythonanywhere.com/api/vX/snippet/############"
}
```

<h2 dir="rtl" align="right">بیشتر بخوانید</h2>
<p dir="rtl" align="right">
 مستندات اصلی کد هاب رو میتونید از <a href="http://codehub.pythonanywhere.com/docs">اینجا</a> دنبال کنید.
</p>
