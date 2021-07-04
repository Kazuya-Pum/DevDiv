'use strict';

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById('submit').addEventListener('click', async () => {
        try {
            const form = document.getElementById('form');
            if (!form.reportValidity()) {
                return;
            }
            loader(true);

            const owner = document.getElementById('owner').value;
            const repo = document.getElementById('repo').value;
            const extension = document.getElementById('extension').value;

            const functions = firebase.app().functions('asia-northeast1');
            const res = await functions.httpsCallable('divination')({ owner, repo, extension });
            document.getElementById('res').innerHTML = res.data.res;
            $('#res-content').collapse();
            loader(false);


            // const res = await fetch('/divination', {
            //     method: 'POST',
            //     headers: { 'Content-Type': 'application/json' },
            //     body: JSON.stringify({ owner, repo, extension })
            // });

            // const res_json = await res.json();

            // document.getElementById('res').innerHTML = res_json.res;

            // $('#res-content').collapse()

            // loader(false);

            const wc_res = await functions.httpsCallable('divination')({ text: res_json['text'] });
            const blob = wc_res.data.blob()

            $('#wordcloud').attr('src', (window.URL || window.webkitURL).createObjectURL(blob))
            $('#wordcloud').collapse()


        } catch (e) {
            console.error(e.message);
        } finally {
            loader(false);
        }
        const form = document.getElementById('form');
        if (!form.reportValidity()) {
            return;
        }
    });

    const loader = (enabled = true) => {
        document.getElementById('loader').style.visibility = (enabled) ? "visible" : "hidden";
    }

})