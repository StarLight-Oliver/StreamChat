import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def AuthYoutube():
    validRequest = True
    youtube = None
    try:
        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "secret.json"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)
    except:
        validRequest = False

    return validRequest, youtube
def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


    print(os.path.abspath(""))
    valid, youtubeAPI = AuthYoutube()
    if not valid:
        os.quit()
    
    request = youtubeAPI.liveBroadcasts().list(
        broadcastStatus="all",
        broadcastType="all",
        part="id,snippet,contentDetails,status"
    )
    response = request.execute()

    response = {
        'kind': 'youtube#liveBroadcastResponse', 
        'etag': 'c_AjheVupvwfkASaI0Ny7LScfr0', 
        'pageInfo': {
            'totalResults': 1, 
            'resultsPerPage': 5
        }, 
        'items': [
            {
                'kind': 'youtube#liveBroadcast', 
                'etag': '3vZZYWyKM6h6bXFb06Y9qd5Dn1I', 
                'id': 'K1aikgHiUes', 
                'snippet': {
                    'publishedAt': '2020-10-13T20:16:48Z', 
                    'channelId': 'UCp3mfPRVMBfEYQuSn6f_utw', 
                    'title': 'StarLight Live Stream', 
                    'description': 'Test', 
                    'thumbnails': {
                        'default': {
                            'url': 'https://i.ytimg.com/vi/K1aikgHiUes/default_live.jpg', 
                            'width': 120, 
                            'height': 90
                        }, 
                        'medium': {
                            'url': 'https://i.ytimg.com/vi/K1aikgHiUes/mqdefault_live.jpg', 
                            'width': 320, 
                            'height': 180
                        }, 
                        'high': {
                            'url': 'https://i.ytimg.com/vi/K1aikgHiUes/hqdefault_live.jpg', 'width': 480, 'height': 360
                        }, 
                        'standard': {
                            'url': 'https://i.ytimg.com/vi/K1aikgHiUes/sddefault_live.jpg', 'width': 640, 'height': 480
                        }, 
                        'maxres': {
                            'url': 'https://i.ytimg.com/vi/K1aikgHiUes/maxresdefault_live.jpg', 'width': 1280, 'height': 720
                        }
                    }, 
                    'scheduledStartTime': '1970-01-01T00:00:00Z', 
                    'actualStartTime': '2020-10-13T20:19:55Z', 
                    'isDefaultBroadcast': False, 
                    'liveChatId': 'Cg0KC0sxYWlrZ0hpVWVzKicKGFVDcDNtZlBSVk1CZkVZUXVTbjZmX3V0dxILSzFhaWtnSGlVZXM'
                }, 'status': {'lifeCycleStatus': 'live', 'privacyStatus': 'unlisted', 'recordingStatus': 'recording', 'madeForKids': False, 'selfDeclaredMadeForKids': False}, 'contentDetails': {'boundStreamId': 'p3mfPRVMBfEYQuSn6f_utw1602620209706691', 'boundStreamLastUpdateTimeMs': '2020-10-13T20:16:49.720000Z', 'monitorStream': {'enableMonitorStream': True, 'broadcastStreamDelayMs': 0, 'embedHtml': '<iframe width="425" height="344" src="https://www.youtube.com/embed/K1aikgHiUes?autoplay=1&livemonitor=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'}, 'enableEmbed': True, 'enableDvr': True, 'enableContentEncryption': False, 'startWithSlate': False, 'recordFromStart': True, 'enableClosedCaptions': False, 'closedCaptionsType': 'closedCaptionsDisabled', 'enableLowLatency': True, 'latencyPreference': 'low', 'projection': 'rectangular', 'enableAutoStart': True, 'enableAutoStop': True}}]}

    if response["pageInfo"]["totalResults"] == 1:
        streamID = response["items"][0]["snippet"]["liveChatId"]
    else:
        print("cry")
        #cry


    print(response)

if __name__ == "__main__":
    main()
