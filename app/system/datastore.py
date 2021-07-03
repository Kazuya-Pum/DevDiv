from google.cloud import datastore


datastore_client = datastore.Client()

def store_repo(owner, repo, sha):
    entity = datastore.Entity(key=datastore_client.key('repo'))
    entity.update({
        'owner': owner,
        'repo': repo,
        'sha': sha,
        
    })

    datastore_client.put(entity)