IMAGE = caydic_sheet
CONTAINER = caydic_sheet_container
PORT = 80

build : 
	docker build -t $(IMAGE) .

run: 
	docker run --name $(CONTAINER) -p $(PORT):1234 -d $(IMAGE)
