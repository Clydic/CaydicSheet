# This is my character of D&D3.5
It was used for one adventure. 

To run this application in debug run:

```
flask --debug run
```

To create a container there is a makefile  
build image:
```
make build
```

run container
```
make create
```

erase container
```
make erase
```

If you wannt to change default parameter:
- IMAGE : name of image you want to build or use
- CONTAINER
- PORT
Example:
```
make run IMAGE=my_image PORT=1236 CONTAINER=my_container name
```

