import Pyro4
from musicstoredb import MusicStoreDB

# Initialize the MusicStoreDB
db_file = 'musicstore.db'
music_store_db = MusicStoreDB(db_file)


# Define the server class with remote methods
@Pyro4.expose
class MusicStoreServer:
    def add_artist(self, name, genre):
        # Implement add_artist method
        # Example: music_store_db.add_artist(name, genre)
        pass

    def add_album(self, name, artist_id, number_of_songs):
        # Implement add_album method
        # Example: music_store_db.add_album(name, artist_id, number_of_songs)
        pass

    # Define more methods for other operations (update, delete, retrieve, etc.)


# Create a Pyro4 Daemon
daemon = Pyro4.Daemon()

# Register the server class with Pyro4
uri = daemon.register(MusicStoreServer)

# Start the Pyro4 nameserver
nameserver = Pyro4.locateNS()
nameserver.register("musicstore.server", uri)

# Run the daemon
print("Server is ready.")
daemon.requestLoop()
