import re
import requests

octodex_json = requests.get('https://sdg-octodex.herokuapp.com/').json()

def octocat_to_html(json):
    return f"""
    <div class="card">
        <a class="card-face" href="{json['link']}">
            <img class="card-img" src="{json['image']}" alt="{json['name']}">
        </a>
        <div class="card-details">
            <span class="card-id">{json['number']}</span>
            <a class="card-name" href="{json['link']}">{json['name']}</a>
            <div class="card-authors">
            {
                "{char(10)}".join([f"<a class='artist-link' href='{author['link']}' target='_blank' rel='nofollow'><img class='artist-img' src='{author['image']}' width='24' height='24'></a>" for author in json['authors']])
            }
            </div>
        </div>
    </div> """

with open("octocats.html", "w") as file:
    for octocat in octodex_json['data']:
        file.write(octocat_to_html(octocat))
