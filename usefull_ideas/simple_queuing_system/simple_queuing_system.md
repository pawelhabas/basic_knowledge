# Simple Queuing System

Example of multi-container system for sending, queuing and processing both occasional and recurrent tasks.

## Containers set

1. The first container is Database for storing tasks. 
For example **Postgres**.
2. The second is main system. Easy to use is **Django**.
3. The third is queuing container. I'll use **RabbitMQ**
4. The forth is worker. I prefere **Celery** worker.
5. The fifth is scheduler. And here we also use **Celery** beat.

## Important in YML
- Set them in one network.
- Set the 'container_name' for each container.
- Set proper 'depends_on', for example:
  - django depends_on postgres
  - celery-worker depends_on rabbitmq & postgres
  - celery-beat depends_on rabbitmq & postgres
- Use the same 'build' for easy cooperate django, celery-worker and celery-beat.
- Good to set restart param.
