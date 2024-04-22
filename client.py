import Pyro4

# Connect to the Pyro4 server
uri = "PYRONAME:musicstore.server"
server = Pyro4.Proxy(uri)

# Example usage of remote methods
server.add_artist("Eminem", "RAP")
server.add_album("The Marshall Mathers LP", 1, 18)

# Call more remote methods as needed

# No need to display results since client doesn't require a user interface
