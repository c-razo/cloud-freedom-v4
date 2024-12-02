#!/bin/bash

echo "Stopping services..."
sudo systemctl stop mariadb || echo "MariaDB service is not running."
sudo systemctl stop nginx || echo "Nginx service is not running."

echo "Removing Nextcloud files..."
sudo rm -rf /var/www/nextcloud

echo "Removing Nextcloud database and user..."
if sudo systemctl is-active --quiet mariadb; then
    sudo mysql -e "DROP DATABASE IF EXISTS nextcloud_db;"
    sudo mysql -e "DROP USER IF EXISTS 'nextcloud_user'@'localhost';"
    sudo mysql -e "FLUSH PRIVILEGES;"
else
    echo "MariaDB is not running; skipping database and user removal."
fi

echo "Removing Nginx configuration..."
sudo rm -f /etc/nginx/sites-available/nextcloud
sudo rm -f /etc/nginx/sites-enabled/nextcloud
sudo systemctl restart nginx || echo "Nginx service failed to restart."

echo "Removing Nextcloud archive..."
if [ -f ~/cloud-freedom-v4/backend/scripts/nextcloud-27.1.1.zip ]; then
    rm ~/cloud-freedom-v4/backend/scripts/nextcloud-27.1.1.zip*
else
    echo "Nextcloud archive not found; skipping removal."
fi

echo "Purging complete. System is ready for a clean test."
