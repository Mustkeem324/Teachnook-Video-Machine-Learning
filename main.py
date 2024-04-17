import requests
import json
import os

def technook():
    try:
        url = "https://learn.teachnook.com/api/course_player/v2/courses/copy-of-machine-learning-december-2022-batch"

        payload = {}
        headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8,zh-TW;q=0.7,zh;q=0.6',
        'cookie': 'twk_uuid_615843d025797d7a8901ec5d=%7B%22uuid%22%3A%221.1vX80ahatGjNgehjDV6vjUs29qkshom5xROW6SXClCo2azLvovtc6CCCUds4NPerRmDDk5n8sOQMwImWydlbu4CzNlw1esgL9s4ImwSYcnYN9VXVjQqKhDA%22%2C%22version%22%3A3%2C%22domain%22%3A%22teachnook.com%22%2C%22ts%22%3A1713332955494%7D; visitor_id=2457883907; __cf_bm=eBA5EiYcY4_BHQ6HZgLauGZZV0IZzjefZmCNZhQcP8g-1713332966-1.0.1.1-c2Q5W8mGOhF_Pme02feC3euPpoHzTbtPU6UNRrM8b9UmBh9mu8ne6yeMSkztxXcbs8Ynf6swzunF_BsB4XhA.A; cf_clearance=rBg99KrW0bW6joCGSjn65pLCLsoHLP9blGoTglwPO.E-1713332968-1.0.1.1-UJlzUaAjQysHravARTWasjq_0IvU2yqGjhewovq38ce7lAPswODhWp0kSSoNhcbX81_GD0qm0SKqVNRyi.dY_w; _thinkific_session=dVlRaStRdXlxdHE5OE9ZakQwSkJZMS9JanY3VTVXSzdRcFZ3M1NFeGRwdmh1dG5VeEw4azIyaUtYQkdHUUx2Q3d3WXF4d1JxRkhCT2V6Rm9oRmlhQUtmQnpJRlBUUG5ERThkeTlWQlB6NWFCQ1BzVklGNHdveWg5Q0hwc09pM2IvS3JNOElhdlZLYnJpL0Q1VWo1M3ZFeEkxM0ROYzBGY0lOdjFqRzhWem1JS3B1Vk82OVRxWERmNm9NQk8yWnVsS0xxOENFVHNBTjVabVZicU5CQ0pjZjk4ZlhRMW52dWczYm9YSVJVNXE2OEhxZ01sck55MWJRcm5pR1BINldmM29pd1pQNkNQMjc3TVdxeCszQUhNN3NkRkpwd2IyL0pKWGd2T0dzZ1dyYkN6dVFXZHZMK0VmOFNYdWE4Q1ZVbE1hRGxFMlI4N3IwZXBVNzN3cXVZdXFwUzNLT290MndweTR4NmVMMlVZOEpORDBwb0ZyVVRCUi9TZ0F6WXRRT1Q0ODkvLzhNWkdFbi9zUFlvM1c0RHV3T015WWlVNFhudE5kM2J4YlZleXBKN2lmeWJTVWhTVEJybVIxSWIvRmZxWk91d1NvY2c4N3hIU25JWld6eElPVVRXYjViQ3FyQS9WWS9nKzRUZ0IwcU5sbXpqOHBic05NeXRaQTVhMDIrUVktLVVUTm1oN1BMWU9xRzltR1BmZ3NtSlE9PQ%3D%3D--18093b5adedf4347ee83c5885f1c323a3c8ec9ac; __cf_bm=cEQInxNZtN5nR0trJS3Al9UhDSZCn_PGMnXaMwf9wzE-1713333831-1.0.1.1-HM_gDuVyewnBPd1Fzl12t.RPzCT9UGaoz9p9980HADRXIRdw0y33wEy2ueGwOZKp4oB7jaAPWnhjs.VSH6PEmw; _thinkific_session=bElVUTdOZk9FZjJNUzdTWVByVktESFRienVPM29uZ3p6WWN6Tm5KRnUyOHRkYmhDR2UvdXJLcnh2eHJvcDUvSW8wMFVidDRKN09sYy8ySXl5dWc1WWRvbjVUVHZmRFNnNithMEd3aExsVjNOWWNBbDFxVURrOE53VGhmOWdXeG1ubG9mMXdENVV4d1B4SzQxanBBWmJKV3FJRlJtZGN0Y0hCbHNHZURZT2haUTdyY2xpQTU5dllDcHZFcEYxSDA0bDdxWkJpT2JFTGN5T1JqWE91VDloMTZveElEVXl1UXlYcHduanZLWUJBczVHcm83MjVJUHFNWGtkN3AxZy82VUgyb2Vtd3FtSTJ0cnBjNGU5MnErcTVFZDB4cmtNN01oWk55OTVJdE5SRHhVa1NHQWVuSElBdzIyZ251aVp6TzVrazJFUWFEYzRVYVUzTHVybmVyYXh3WmhOUFYxa3BXejI4cFNOV2MrTnhKWFhhb2JaTVYzR3o5REhWOTVTZ3U3c2NMVHJGV3hRQVU1bmZPWElldjhkTmV0NkhjVkJvVE1JMktBTmw4bzlyZG4xbFJZdUZ4aEZqeFhEQkpxUHFGdWhCRGVDb3B3R1RPNW1NMi9vT01MbVcwOC9hakRWVWRTQW50RWFQcm5NVitlYTU3ZWFndVRianMxQzE5TWdENUQtLW5lY1FFUzZQdGhWYXlXOS9FVzBpYUE9PQ%3D%3D--2d2ff49c45b4faf66c62964ed91514aac7ec8896',
        'dnt': '1',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0ODEzMzgiLCJhcCI6IjU5NDMzNjg0NiIsImlkIjoiNDQ3YzFjYTI1MmFlNmY0OCIsInRyIjoiZGQwMzUzYzNiODRkMDc1YzIwMDYzMjE4ZTAyZWJhMjYiLCJ0aSI6MTcxMzMzMzgwMjMzOSwidGsiOiIzNDE0NzgzIn19',
        'referer': 'https://learn.teachnook.com/courses/take/copy-of-machine-learning-december-2022-batch/lessons/42856305-class-5',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-dd0353c3b84d075c20063218e02eba26-447c1ca252ae6f48-01',
        'tracestate': '3414783@nr=0-1-3481338-594336846-447c1ca252ae6f48----1713333802339',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-client-id': 'KOBAYASHI',
        'x-newrelic-id': 'VwIPUFVQABAFUFdTAAUFV1Q=',
        'x-requested-with': 'XMLHttpRequest',
        'x-thinkific-client-app-version': '3d23908d62f33242ba87a2b36949fbb7988e34d1',
        'x-thinkific-client-date': '2024-04-17T06:03:22.339Z'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == 200:
            response_data = json.loads(response.text)
            contents = response_data['contents']
            video_urls = []
            for item in contents:
                contentable = item.get("contentable") 
                if contentable:
                    print(contentable)
                    url2 = "https://learn.teachnook.com/api/course_player/v2/lessons/"+str(contentable)

                    payload2 = {}
                    headers2 = {
                        'accept': 'application/json',
                        'accept-language': 'en-US,en;q=0.9,ru;q=0.8,zh-TW;q=0.7,zh;q=0.6',
                        'cookie': 'twk_uuid_615843d025797d7a8901ec5d=%7B%22uuid%22%3A%221.1vX80ahatGjNgehjDV6vjUs29qkshom5xROW6SXClCo2azLvovtc6CCCUds4NPerRmDDk5n8sOQMwImWydlbu4CzNlw1esgL9s4ImwSYcnYN9VXVjQqKhDA%22%2C%22version%22%3A3%2C%22domain%22%3A%22teachnook.com%22%2C%22ts%22%3A1713332955494%7D; visitor_id=2457883907; __cf_bm=eBA5EiYcY4_BHQ6HZgLauGZZV0IZzjefZmCNZhQcP8g-1713332966-1.0.1.1-c2Q5W8mGOhF_Pme02feC3euPpoHzTbtPU6UNRrM8b9UmBh9mu8ne6yeMSkztxXcbs8Ynf6swzunF_BsB4XhA.A; cf_clearance=rBg99KrW0bW6joCGSjn65pLCLsoHLP9blGoTglwPO.E-1713332968-1.0.1.1-UJlzUaAjQysHravARTWasjq_0IvU2yqGjhewovq38ce7lAPswODhWp0kSSoNhcbX81_GD0qm0SKqVNRyi.dY_w; _thinkific_session=dnA0Wm5iV2ljNnNBOGw4SVBTRm0zSGlmTWFva2ZQd3NIM2RkN0tBcVp5Q1M5Uy8rZzBMa3YvOUgwWWRkTzhpcXlEemEyYUJTd0hINldIckpSRDRyWmd5ZDJlY2tzemJkUmlORzRaUjk5YUM5U3JFMFlhZHY3VjZQbFBkQWRvRUJKbHVlUlArWGV2c0Iwcll6UUZhQ2NUOXJOV044RWw5Q3hWTGtlUlRBUjBLSjhjbDUwSC9LdEJPOE0vTTJVa3ZGRGVvdnppbXdUQjQ0bGs5RHZRZVdqbmFhR0NJN056S3pVTGlzYWdGd083YkxRa2xTSFc1NmdQRUhBYzE0OFEzMWZ1MHFCd3RYbFBnVmJrZUJNTGl5VUJMUWw1clppUktGUGFSNEhXWjd4UE5wTWpyRVczRkJRR3pYOHJEWWpBQkxCVmNOUlRlNGx2eThQSncrN2pGOGl2UFYvL1RWOUZneU45WHpycG02dnJFWGRza2F4Um5RaEZ1RUdiNGlXWDg3WnFTNzRkNmZNYVRsNUIrcGlyUThGc1VpM0s4TERTMTI2V2NYcHVwOGg3c0s0QWVQbVlQVjBLNVM3YTRwYytwMnNFeHovZC9aWUEvdkxJVWdOcFlMdXRKNmNHUlhkY2RVczA3K1huTTFpWlBsTE9BcWp4clNOUWdYSGd3Tm1EczAtLUxkRE81UkZjeHNNcFFMbEU1STlLQ0E9PQ%3D%3D--809e9093904ab4ed00535f185f12b12026eb9e0a; __cf_bm=zCN9b89Omc3EXQIXrgQvIH7b0.IuDNPYFyLrbbxBRIw-1713333318-1.0.1.1-JtBXJTkynspuKA9ZAVN4h6QFFw0Eqgq0CvUBw3R7MyExbA5vQy4qn5XMYORlCIYV_ebr0KFizJhW_yfPUibTiQ; _thinkific_session=RG1PTWtvdmRlaXBJc0VzdFJxMjVjTVAvcWFDQVlaYitOVmhkV1N6bnVETHVCU1ZxRDU5cksrZTBnZ0QrMDllcHZ4SkpjSEVRRTY4bEgzR1NPSndxWWdrOU5qY3l2WlVtK0dmVlhNbEpqdldNQXFZOE5KaVVEaXpST0Z3T0dPYVAreE0yS2JKRTcxY1EwYjZVanlaVDk4TTdtQXo0blpGZ3FlellXTGlEOEowVy9NODRHUjBSOUNoallQMlVVc2tvK3FGbmF5RElhRDhHQ3hWcW1GT3Y0dVZiMTNtczg2YWFGNkR5cHhZaHdoa1ZTcVRISUhHSEU1L2p0bE85S3JEd3cwbzU4R3pnT3g0RHczZU1GVW43eDhXMlVnSnp0ZFdialMyUmM5Umhia1FVWHR1RnRqVEhKOWs0aHdaeFRVUnpuMjh6a0lRQzZqa3lsT2VZa2RWS1FkOUJzV3hTblhhaWFKSGcxdHNrS2E4OStEYTFhSFFRV3FaMm01ZTRGMDN3enFMSnhYNmNWcHN5QllFNDhwOUdSZlJmOHdCd3lKdDd5RVZjbHZZSzkyaXNnQXlQWU9hYmFGeitsZWZmUHdiU3E2M3dDRkp0c1Z1SzRxYkNSWnpuaUtoQUV0bXRURVE3Umd6V244ckVDVzhsU3RGeWg5OXRRbXNqcThNS0xlNG4tLWZoQmZwa1hFUGV5Mnd2dGphZVpYcXc9PQ%3D%3D--8c06feaf8738a463719ee2a9b4e20711f880bb67',
                        'dnt': '1',
                        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0ODEzMzgiLCJhcCI6IjU5NDMzNjg0NiIsImlkIjoiOWNjNjRhY2MxYmZkNWQ5ZSIsInRyIjoiZDA2OWI1ZDRiNDhlZGFiODM4MDdkNTM3ZDA1MjcwMGMiLCJ0aSI6MTcxMzMzMzA1NjU5NiwidGsiOiIzNDE0NzgzIn19',
                        'referer': 'https://learn.teachnook.com/courses/take/copy-of-machine-learning-december-2022-batch/lessons/42540576-induction-session',
                        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Linux"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'traceparent': '00-d069b5d4b48edab83807d537d052700c-9cc64acc1bfd5d9e-01',
                        'tracestate': '3414783@nr=0-1-3481338-594336846-9cc64acc1bfd5d9e----1713333056596',
                        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                        'x-client-id': 'KOBAYASHI',
                        'x-newrelic-id': 'VwIPUFVQABAFUFdTAAUFV1Q=',
                        'x-requested-with': 'XMLHttpRequest',
                        'x-thinkific-client-app-version': '3d23908d62f33242ba87a2b36949fbb7988e34d1',
                        'x-thinkific-client-date': '2024-04-17T05:50:56.596Z'
                        }

                    response = requests.request("GET", url2, headers=headers2, data=payload2)
                    try:
                        video_url = json.loads(response.text)['lesson']['video_url']
                        video_urls.append(video_url)
                    except Exception as e:
                        print(f"No downloaded it pdf")
                        continue    
                else:
                    print("No 'contentable' attribute found for this item")
            return video_urls
        else:
            print("Failed to fetch data:", response.status_code)
            print(response.text)
    except Exception as e:
        print(e)
               

def save_video_urls(json_file):
    video_urls = technook()
    with open(json_file, 'w') as f:
        json.dump(video_urls, f)
    print(f"Video URLs saved to {json_file}")

json_file = "video_urls.json"
save_video_urls(json_file)
