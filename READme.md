#   Real estate management system with djangorestframework

## Endpoints

###   login
```
http://localhost:8000/api/v1/token/login
```
### sign-up
```
http://localhost:8000/api/v1/users/
```

### post-contact
```
http://localhost:8000/api/v1/createcontact/
```
### view-contact

```
http://localhost:8000/api/v1/viewcontact/
```
### create-listing

```
http://localhost:8000/api/v1/createlisting/
```

### view details of listing

```
http://localhost:8000/api/v1/listings/single-room-apartment/
```

### create realtor
```
http://localhost:8000/api/v1/createrealtor/
```
### view realtor
```
http://localhost:8000/api/v1/realtors/
```




# Features
* Full Crud fuctionality
* User Authentication with auth token using TokenAuthentication
* django-cors-headers for handling the server headers required for Cross-Origin Resource Sharing (CORS).


# Download & Setup Instructions

# Setup for Django

* 1 - Clone project: 
```
git clone https://github.com/patoski716/Real-estate-with-djangorestframework.git
```
```
cd Real-estate-with-djangorestframework
```
* 2 - Create virtual environment: 

```
virtualenv myenv
```
```
myenv\scripts\activate
```
```
pip install -r requirements.txt
```
```
python manage.py runserver
```

