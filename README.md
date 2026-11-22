# SwapnaLoka — the pen site of Swapnil Sapre

> **Builder · Innovator · Entrepreneur**
> Semiconductor, embedded-systems and deep-tech AI veteran · Advisor · Consultant · Coach · Program leader · Poet · Musician

SwapnaLoka (स्वप्नलोक, "the world of dreams") is Swapnil Sapre's personal profile site. It's a single fast, static page with no build step, plus a downloadable profile in PDF and Word.

---

## Who

Swapnil Sapre has spent **24+ years** in semiconductors and embedded systems, taking products **from spec to silicon to volume production**:

| | |
|---|---|
| **Now** | AVP – Engineering, ultra-low-power edge-AI processors (2020–) · Independent consultant & advisor (2026–) |
| **Before** | Western Digital (system architect, product line manager: SD / microSD / SSD / NVMe) · AMD · Freescale/NXP · Mindtree · Wipro |
| **Builds** | [Chiluka](https://chiluka.online) · [SwaraKul](https://swarakul.online) · **Damruki**: School of Rhythm & Seven Swaras (founder) · [**Suphala Care**](https://suphalacare.com): holistic nutrition & wellness with Dr Suguna Sapre, plus the [SuViva](https://suphalacare.com/suviva/) network |
| **Writes** | *Nuts and Bolts of Open Hardware* · *Python — a Kid's and Hardware Engineer's Perspective* · *Understanding Indian Music through Rhythms* · Hindi poetry *Noorana* and *Chuski* (as "Noor" / "Sopaan Noor") |
| **Plays** | Tabla (Khairagarh, Shri Suresh Samant, Dr. Aneesh Pradhan) and Mridangam (late Dr. Nandyala Ramamurthy) · album *Raam Gunjan* |
| **Studied** | M.S. VLSI CAD (Manipal) · IIM Bangalore PGSEM coursework · IIT Bombay DLP Embedded Systems · B.E. E&TC (BIT Durg) |

**Find him on:** [LinkedIn](https://www.linkedin.com/in/swapnils29/) · [YouTube: Bansuri Beats](https://youtube.com/playlist?list=PLEvT8t4QvqOaNjM0dtJCjaw-OOXxShNex) · [Facebook](https://www.facebook.com/swapsap1) · [Books on Amazon](https://www.amazon.in/s?i=stripbooks&rh=p_27%3ASwapnil%2BSapre&ref=dp_byline_sr_book_1)

---

## Profile documents

| File | What |
|---|---|
| [docs/SwapnaLoka_Profile_Swapnil_Sapre.pdf](docs/SwapnaLoka_Profile_Swapnil_Sapre.pdf) | 3-page designed profile (A4) |
| [docs/SwapnaLoka_Profile_Swapnil_Sapre.docx](docs/SwapnaLoka_Profile_Swapnil_Sapre.docx) | Same content as an editable Word document |
| [docs/Swapnil_Sapre_Conference_OnePager.pdf](docs/Swapnil_Sapre_Conference_OnePager.pdf) | Speaker / conference one-pager |
| [docs/Swapnil_Profile_Music_and_Arts.pdf](docs/Swapnil_Profile_Music_and_Arts.pdf) | Music & arts biography |

Both profile files are generated from one content source, [tools/build_profile.py](tools/build_profile.py). To change the wording, edit the lists at the top of that script and rebuild:

```bash
pip install python-docx reportlab
python tools/build_profile.py
```

---

## Site structure

```
index.html              single-page site (all copy lives here)
assets/css/style.css    design tokens (navy · gold · saffron · cream), light + dark mode
assets/js/main.js       mobile menu, scroll reveal, footer year
assets/img/             portrait, SwapnaLoka logo, favicon
docs/                   downloadable PDFs / DOCX
tools/build_profile.py  generates the profile PDF + DOCX
```

Page sections: **Hero → About → Builder (ventures, with Damruki and Suphala Care in focus) → Advisory / consulting / coaching + expertise → Career timeline, education, papers → Books & newsletter → Music (YouTube playlist embed) → Connect**.

### Preview locally

```bash
python -m http.server 8080      # then open http://localhost:8080
```

Serve it over http as above. If you open `index.html` straight from disk, the YouTube embed refuses to play ("Error 153").

### Publish (GitHub Pages)

1. Push this repo to GitHub (`swap111/profile`).
2. **Settings → Pages → Deploy from branch → `main` / root**.
3. The site appears at `https://swap111.github.io/profile/`. For a custom domain (for example `swapnaloka.in`), add a `CNAME` file and point DNS at GitHub Pages.

It works the same on any static host (Hostinger, Netlify, Cloudflare Pages). Just upload the folder.

---

## Privacy notes

- The site and profile list only **public contact routes**: LinkedIn, YouTube, Facebook, Amazon, and the email already used on the conference one-pager. **No phone number.**
- The full executive resume (`Resume_*.docx/pdf`) contains a phone number and personal emails. It stays local and is **git-ignored**, so it's never published.

---

## Ideas for next steps

- Custom domain, for example `swapnaloka.in`, and an Open Graph share image.
- Real book covers and ASIN links once the Amazon listings are confirmed.
- A "Writing" feed that pulls the latest SwapnaLoka newsletter articles from LinkedIn.
- Hindi poetry page (Devanagari) with a few selected poems by "Noor".
- Testimonials, using the LinkedIn recommendations.
- A booking or contact form for advisory and speaking enquiries.

---

© Swapnil Sapre · SwapnaLoka
