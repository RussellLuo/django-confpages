# Django ConfPages

A Django app for serving configurable pages.


## Philosophy

Most of the time, frontend pages are more changeful than backend services.

While the pages (also known as `templates` in Django) and services (also known as `views` in Django) are always strongly coupled in Django, you have to deploy your Web applications every time the pages are changed or even tweaked.

By decoupling the pages and services, and by making the pages to be configurable, you can change the pages dynamically without any deployment step as long as the services are not changed. Even there are times that the services need to be changed, you can still benefit from the decoupling and the configurability, which will give you a lower deployment frequency.


## License

[MIT][1]


[1]: http://opensource.org/licenses/MIT
