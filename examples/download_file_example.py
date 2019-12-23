# download test
import sys
import demisto_client.demisto_api


def main():
    if len(sys.argv) != 2 or (len(sys.argv) == 2 and (sys.argv[1] == '-h' or sys.argv[1] == '--help')):
        print("Usage: {} <entry_id>".format(sys.argv[0]))
        sys.exit(1)
    eid = sys.argv[1]
    print("Downloading file from entry id: {}".format(eid))
    api_key = None  # set to your 'YOUR_API_KEY' or set environment variable: DEMISTO_API_KEY
    base_url = None  # set to your 'http://DEMISTO_HOST' or set environment variable: DEMISTO_BASE_URL

    api_instance = demisto_client.configure(base_url=base_url, api_key=api_key, debug=False)
    res_download = api_instance.download_file(eid)
    print("Download file is available at: {}".format(res_download))
    print("Downloading again the file but not storing to disk (_preload_content=False)...")
    res_download = api_instance.download_file(eid, _preload_content=False)
    print("Download file size: {}".format(len(res_download.data)))


if __name__ == "__main__":
    main()
