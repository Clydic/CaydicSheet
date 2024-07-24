IMAGE = caydic_sheet
CONTAINER = caydic_sheet_container
PORT = 5000

build : 
	docker build -t $(IMAGE) .

run: 
	docker run --name $(CONTAINER) -p $(PORT):1234 -d $(IMAGE)