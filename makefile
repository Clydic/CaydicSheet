IMAGE = caydic_sheet
CONTAINER = caydic_sheet_container
PORT = 8080

build : 
	docker build -t $(IMAGE) .

run: 
	docker run  --restart always --name $(CONTAINER) -p $(PORT):1234 -d $(IMAGE)

erase:
	docker rm -f $(CONTAINER)