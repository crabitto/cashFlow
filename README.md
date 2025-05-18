
# FinTrack – personīgās finanšu uzskaites sistēma

---

## Projekta apraksts

FinTrack ir tīmekļa lietotne, kas palīdz pārvaldīt personīgos ienākumus un izdevumus, sniedzot skaidru pārskatu par jūsu finanšu bilanci. Programmatūra ļauj ērti pievienot jaunas finanšu transakcijas, pārlūkot esošos ierakstus ar iespēju tos filtrēt un kārtot pēc datuma vai kategorijas, kā arī ģenerēt statistikas grafikus, lai vieglāk saprastu savas naudas plūsmas.

Šī sistēma ir izstrādāta, lai automatizētu ikdienas finanšu uzskaiti un palīdzētu lietotājam pārskatīt savus izdevumus un ienākumus vienuviet, bez nepieciešamības izmantot sarežģītas grāmatvedības programmas.

---

## Izmantotās tehnoloģijas un bibliotēkas

- **Python + Flask** – lietotnes servera pamatā, kas nodrošina datu apstrādi un tīmekļa saskarni.
- **HTML + Bootstrap** – tīmekļa lietotāja interfeiss, kas padara lietotni vizuāli pievilcīgu un lietotājam draudzīgu.
- **json** – dati tiek saglabāti JSON formātā, kas ir viegli lasāms un pārvaldāms, nodrošinot datu uzglabāšanu bez datubāzes.
- **datetime** – datumu apstrādei un pareizai to attēlošanai un filtrēšanai.
- **matplotlib** – vizualizācijas bibliotēka, ar kuru tiek veidoti grafiki, lai attēlotu finanšu statistiku.
- **os** – failu sistēmas darbībām, piemēram, datu failu atrašanai un pārlūkošanai.

---

## Datu struktūras

Datu ieraksti tiek glabāti JSON formātā kā saraksts ar vārdnīcām, kur katram ierakstam ir šādas atslēgas:

| Atslēga      | Apraksts                      | Piemērs        |
|--------------|-------------------------------|----------------|
| `type`       | "income" vai "expense"        | `"income"`     |
| `amount`     | skaitlis, kas norāda summu    | `500`          |
| `category`   | kategorijas nosaukums         | `"Alga"`       |
| `description`| īss apraksts                  | `"Mēneša alga"`|
| `date`       | datums formātā YYYY-MM-DD     | `"2025-05-01"` |

Papildus tam projekta kodā datu apstrāde notiek, izmantojot klasēs iekapsulētas datu struktūras un sarakstus, kas nodrošina efektīvu datu manipulāciju.

---

## Lietošanas instrukcija

### Sākumlapa

Atveriet lietotni, lai redzētu pārskatu par kopējo bilanci — cik daudz ir ienākuši un cik iztērēti līdzekļi.

### Jauna ieraksta pievienošana

Izvēlieties **"Add Record"** un aizpildiet formu, norādot summu, kategoriju, aprakstu un datumu. Var pievienot gan ienākumus, gan izdevumus.

### Ierakstu pārlūkošana

Dodieties uz **"All Records"**, kur varat skatīt visus ierakstus, filtrēt tos pēc datuma vai kategorijas, kā arī kārtot tos pēc vēlamā kritērija.

### Statistika un grafiki

Izvēlieties sadaļu **"Home"**, lai redzētu vizualizācijas par izdevumiem un ienākumiem dažādās kategorijās un laika posmos.

---

## Projekta struktūra

```
fintrack/
│
├── app.py                ← Flask serveris
├── templates/            ← HTML lapu šabloni
├── static/               ← CSS un citi statiskie faili
├── data/
│   └── records.json      ← saglabātie dati
├── README.md             ← šī dokumentācija
└── requirements.txt      ← Python bibliotēkas
```

---

## Versiju kontrole un sadarbība

Visa projekta attīstība tiek veikta, izmantojot **GitHub**, kurā tiek glabāts kods un dokumentācija. Tas ļauj izsekot visām izmaiņām un strādāt komandā efektīvi.
