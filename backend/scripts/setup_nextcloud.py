import os
import subprocess

def run_command(command):
    """Run a shell command."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        exit(1)

<<<<<<< HEAD
def install_dependencies():
    """Install necessary dependencies for Nextcloud."""
    print("Installing Nginx, PHP, MariaDB, and other dependencies...")
    run_command("sudo apt update && sudo apt upgrade -y")
    run_command("sudo apt install -y nginx php-fpm php-mysql php-zip php-gd php-mbstring php-curl php-xml php-bcmath mariadb-server unzip")
=======
def start_mariadb():
    """Ensure MariaDB is running."""
    print("Checking if MariaDB is running...")
    try:
        run_command("sudo systemctl start mariadb")
        print("MariaDB started successfully.")
    except:
        print("Failed to start MariaDB. Please ensure it's installed correctly.")
        exit(1)

def install_dependencies():
    """Install necessary dependencies for Nextcloud."""
    print("Installing required dependencies...")
    run_command("sudo apt install -y --no-install-recommends wget nginx php-fpm php-mysql php-zip php-gd php-mbstring php-curl php-xml php-bcmath mariadb-server unzip")
>>>>>>> 195c2b7 (Checkpoint: Working purge and setup scripts)

def configure_database(db_name, db_user, db_password):
    """Configure MariaDB for Nextcloud."""
    print("Configuring MariaDB...")
    commands = f"""
    sudo mysql -e "CREATE DATABASE {db_name};"
    sudo mysql -e "CREATE USER '{db_user}'@'localhost' IDENTIFIED BY '{db_password}';"
    sudo mysql -e "GRANT ALL PRIVILEGES ON {db_name}.* TO '{db_user}'@'localhost';"
    sudo mysql -e "FLUSH PRIVILEGES;"
    """
    run_command(commands)

def configure_nginx():
    """Set up Nginx configuration for Nextcloud."""
    print("Configuring Nginx for Nextcloud...")
    nginx_config = """
    server {
        listen 80;
        server_name localhost;

        root /var/www/nextcloud;
        index index.php index.html;

        location / {
            try_files $uri $uri/ /index.php;
        }

        location ~ \.php$ {
            include snippets/fastcgi-php.conf;
            fastcgi_pass unix:/var/run/php/php-fpm.sock;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            include fastcgi_params;
        }

        location ~ /\.ht {
            deny all;
        }
    }
    """
    # Write the Nginx config file with elevated privileges
    run_command(f"echo '{nginx_config}' | sudo tee /etc/nginx/sites-available/nextcloud > /dev/null")
<<<<<<< HEAD
    run_command("sudo ln -s /etc/nginx/sites-available/nextcloud /etc/nginx/sites-enabled/")
=======
    run_command("sudo ln -sf /etc/nginx/sites-available/nextcloud /etc/nginx/sites-enabled/")
>>>>>>> 195c2b7 (Checkpoint: Working purge and setup scripts)
    run_command("sudo nginx -t")
    run_command("sudo systemctl restart nginx")

def setup_nextcloud():
    """Download and set up Nextcloud."""
    print("Setting up Nextcloud...")
    run_command("wget https://download.nextcloud.com/server/releases/nextcloud-27.1.1.zip")
    run_command("sudo unzip nextcloud-27.1.1.zip -d /var/www/")
    run_command("sudo chown -R www-data:www-data /var/www/nextcloud")
    run_command("sudo chmod -R 755 /var/www/nextcloud")

def run_installation():
    """Run the complete installation."""
    print("Starting the Nextcloud installation process...")
    
    # Hardcoded values for testing
    db_name = "nextcloud_db"
    db_user = "nextcloud_user"
    db_password = "strongpassword"

<<<<<<< HEAD
=======
    # Ensure MariaDB is running
    start_mariadb()
    
>>>>>>> 195c2b7 (Checkpoint: Working purge and setup scripts)
    # Execute installation steps
    install_dependencies()
    configure_database(db_name, db_user, db_password)
    configure_nginx()
    setup_nextcloud()
    print("Nextcloud installation complete. Access it in your browser.")

if __name__ == "__main__":
    run_installation()
<<<<<<< HEAD

=======
>>>>>>> 195c2b7 (Checkpoint: Working purge and setup scripts)
