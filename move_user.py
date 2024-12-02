
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE
import sys

def move_user(ad_username, target_ou, server_ip, ad_user, ad_password):
    try:
        # Connect to the AD server
        server = Server(server_ip, get_info=ALL)
        conn = Connection(server, user=f"CN={ad_user},CN=Users,DC=test,DC=com", password=ad_password, auto_bind=True)

        # Search for the user to get their current DN
        conn.search(
            search_base='DC=test,DC=com',
            search_filter=f'(cn={ad_username})',
            attributes=['distinguishedName']
        )
        
        if not conn.entries:
            print(f"User '{ad_username}' not found in the domain.")
            return

        user_dn = conn.entries[0].distinguishedName.value  # Retrieve user DN dynamically
        target_dn = f"OU={target_ou},DC=test,DC=com"

        # Move operation
        move_result = conn.modify_dn(user_dn, f"CN={ad_username}", new_superior=target_dn)
        
        if move_result:
            print(f"Successfully moved user '{ad_username}' to '{target_ou}'")
        else:
            print(f"Failed to move user '{ad_username}': {conn.result['description']}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: move_user.py <username> <target_ou> <server_ip> <ad_user> <ad_password>")
        sys.exit(1)

    username = sys.argv[1]
    target_ou = sys.argv[2]
    server_ip = sys.argv[3]
    ad_user = sys.argv[4]
    ad_password = sys.argv[5]

    move_user(username, target_ou, server_ip, ad_user, ad_password)
