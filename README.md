# Scrapy-reality-project
Utilizing Scrapy to scrape data, which is then stored in a PostgreSQL database and visualized through an HTML-based web server, all within a Dockerized environment.

## How to Launch:

### Prerequisites
1. Install Docker on your system.
2. Install Git (if not already installed).

### Steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/stehlfi1/Scrapy-reality-project.git
    ```
  
2. **Navigate to the project directory:**
    ```bash
    cd Luxoris
    ```

3. **Build and Launch the Docker Compose:**
    ```bash
    docker-compose up --build
    ```
  
4. **Access App:**
    - Open your web browser and go to `http://localhost:8070`.

5. **To Stop the Services:**
    ```bash
    docker-compose down
    ```

### Troubleshooting:
1. If facing authentication errors, make sure to restart the Docker containers.
    ```bash
    docker-compose down
    docker-compose up
    ```
