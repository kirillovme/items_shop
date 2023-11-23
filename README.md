# Items Shop

This project is a test task for Ranks.

## Main Technologies Used

- Python
- Django
- PostgreSQL
- Stripe API
- Docker

## Deploying the Project

### Requirements
- Docker and Docker Compose installed
- GNU Make (https://www.gnu.org/software/make/)

### Instructions:
1. Clone the repository
   ```bash
   git clone https://github.com/kirillovme/items_shop.git
   ```
2. Rename .env.example to .env and complete empty fields
3. Start the containers
   ```bash
   make up-d
   ```
4. Create superuser
    ```bash
    make createsuperuser
    ```
5. Visit http://localhost:8000/admin/ and do following:
- Create item or items in Items
- Create order or orders in Orders
- Create discount or discounts in Discounts
- Create tax or taxes in Taxes
6. For item purchase visit http://localhost:8000/item/1/
7. For order checkout visit http://localhost:8000/order/1/
