import random


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0

        # maps IDs to User Objects. Users represent vertices in this case.
        self.users = {}

        # These are our edges. Edges are the connections ("friendships") between users.
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # !!!! IMPLEMENT ME
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User-{i + 1}")

        # Create friendships
        # Generate ALL possible friendships.
        # Avoid duplicate friendships.

        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):

                # user_id == user_id_2 cannot happen.
                # If friendship between user_id and user_id_2 already exists
                #   don't add friendship between user_id_2 and user_id

                possible_friendships.append((user_id, friend_id))
        # Randomly select x friendships.

        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # print("possible friendships: ", possible_friendships)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        This is going to be a breadth first traversal of the graph returning the shortest path between users A and B.

        """

        # Step 1) Create a queue.
        queue = []

        # Step 2) Add a 'visited' dict to weed out duplicates.
        visited = {}

        # Step 3) Add the starting vertex.
        queue.append([user_id])

        while len(queue) > 0:
            
            path = queue.pop(0)
            

            if current_vertex not in visited:
                path.append(current_vertex)

            print(current_vertex)

            # Get the friends of the current user.
            friends = self.friendships[user_id]

            print(queue)

            return queue
            # for i in friends:
            #     queue.append(i)

            # visited[user_id] = path

            # print(f"This returns the friends for {user_id}: {friends}")

        # friends = self.friendships[user_id]

        # print("friends: ", friends)
        # example_visited = {

        #     2: [1, 2],
        #     3: [1, 2, 3],

        #     }
        # Note that this is a dictionary, not a set

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
