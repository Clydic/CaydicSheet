IMAGE = caydic_sheet
CONTAINER = caydic_sheet_container
PORT = 8080

build : 
	sudo docker build -t $(IMAGE) .

run: 
	sudo docker run  --restart always --name $(CONTAINER) -p $(PORT):1234 -d $(IMAGE)

erase:
	sudo docker rm -f $(CONTAINER)
