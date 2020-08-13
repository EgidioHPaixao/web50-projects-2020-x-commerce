# web50-projects-2020-x-commerce
Harvard CS50 course - Project 2 - eBay-like e-commerce auction site

https://cs50.harvard.edu/web/2020/projects/2/commerce/

## Steps

* Added .gitignore file to keep database locally
* Install pillow to work with uploaded image files, running ``` python -m pip install Pillow ```

## Useful links

https://studygyaan.com/django/how-to-upload-and-display-image-in-django

https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django



 ## Troubleshoots

 #### The view didn't return an HttpResponse object. It returned None instead

 If you get _"The view \*\*\*\* didn't return an HttpResponse object. It returned None instead"_, it's probably because **your view method doesn't have a "return render" command**. [Check here the discussion](https://stackoverflow.com/questions/26258905/the-view-didnt-return-an-httpresponse-object-it-returned-none-instead) 
 
 #### jango.db.utils.IntegrityError: NOT NULL constraint failed:

 Instead of saving the form directly ...
 ```
 form.save()
 ```
 ...try to do the following:
```
        newItem = form.save(commit=False)
        newItem.user = request.user <--- here you put all foreign key fields
        newItem.save()
```