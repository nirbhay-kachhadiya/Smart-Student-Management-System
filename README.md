<div align="center">

I see the issue. The HTML isn't rendering as code because it's being interpreted as actual HTML. To display HTML as code in the README, wrap it with markdown code fences using triple backticks and specify the language:

```html
<img src="https://capsule-render.vercel.app/api?type=waving&color=0078D7&height=220&section=header&text=Student%20Management%20System&fontSize=45&animation=fadeIn&fontAlignY=38&desc=Smart%20%7C%20Fast%20%7C%20Reliable&descAlignY=55&descAlign=62" alt="Student Management System Header" width="100%"/>

<p>
<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-Database-green?style=for-the-badge&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/Maintained%3F-Yes-lightgrey?style=for-the-badge" />
</p>
```

This will display the HTML code as text instead of rendering it.
