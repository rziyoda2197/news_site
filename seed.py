import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'news_site.settings'
django.setup()

from django.contrib.auth.models import User
from news.models import Category, Post

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@newsportal.uz', 'admin123')
    print('Superuser created')

# Create categories
cats = ['Siyosat', 'Iqtisodiyot', 'Sport', 'Texnologiya', 'Jamiyat', 'Madaniyat']
for c in cats:
    cat, created = Category.objects.get_or_create(name=c, slug=c.lower())
    if created:
        print(f'Category: {c}')

# Create sample posts
admin_user = User.objects.get(username='admin')

posts_data = [
    {
        'title': 'Ozbekistonda raqamli iqtisodiyot rivojlanmoqda',
        'slug': 'raqamli-iqtisodiyot',
        'body': 'Ozbekistonda raqamli iqtisodiyot sohasida katta ozgarishlar sodir bolmoqda. Hukumat tomonidan qabul qilingan yangi dastur IT sohasini rivojlantirish, suniy intellekt texnologiyalarini joriy etish va raqamli xizmatlarni kengaytirish boyicha aniq chora-tadbirlarni belgilab berdi. Mutaxassislarning fikricha, bu dastur mamlakat iqtisodiyotiga ijobiy tasir korsatadi.',
        'category': 'Iqtisodiyot',
        'tags': 'texnologiya, iqtisodiyot, raqamli',
    },
    {
        'title': 'Futbol boyicha jahon chempionati 2026',
        'slug': 'futbol-jahon-chempionati-2026',
        'body': 'FIFA Jahon Chempionati 2026 yilda AQSh, Kanada va Meksikada otkaziladi. Ozbekiston terma jamoasi ham bu musobaqada ishtirok etish uchun saralash oyinlarida kurashmoqda. Jamoamiz oxirgi oyinlarda ajoyib natijalar korsatdi va muxlislar umid bilan kutishmoqda.',
        'category': 'Sport',
        'tags': 'futbol, sport, jahon',
    },
    {
        'title': 'Suniy intellekt talimda',
        'slug': 'suniy-intellekt-talimda',
        'body': 'Suniy intellekt texnologiyalari talim sohasida keng qollanila boshlanmoqda. Bugungi kunda koplab universitetlar AI asosidagi oquv dasturlarini joriy etmoqda. Bu texnologiyalar talabalar uchun shaxsiylashtirilgan talim imkoniyatlarini yaratmoqda.',
        'category': 'Texnologiya',
        'tags': 'texnologiya, talim, AI',
    },
    {
        'title': 'Toshkentda yangi metro liniyasi ochildi',
        'slug': 'yangi-metro-liniyasi',
        'body': 'Toshkent shahri metro tizimining yangi liniyasi bugun rasmiy ravishda ochildi. Yangi liniya shaharning janubiy qismini markaz bilan boglaydi va har kuni minglab yolovchilar uchun qulay transport imkoniyatini yaratadi. Bu loyiha shahar infratuzilmasini rivojlantirishning muhim qadamidir.',
        'category': 'Jamiyat',
        'tags': 'toshkent, metro, transport',
    },
    {
        'title': 'Ozbekiston madaniyat festivali',
        'slug': 'ozbekiston-madaniyat-festivali',
        'body': 'Samarqandda xalqaro madaniyat festivali boshlandi. 30 dan ortiq mamlakatdan sanat vakillari ishtirok etmoqda. Festival doirasida konsertlar, korgazmalar va master-klasslar tashkil etilgan. Bu tadbir Ozbekiston madaniyatini jahonga tanishtirish maqsadida otkazilmoqda.',
        'category': 'Madaniyat',
        'tags': 'madaniyat, festival, samarqand',
    },
    {
        'title': 'Yangi qonun loyihasi muhokama qilinmoqda',
        'slug': 'yangi-qonun-loyihasi',
        'body': 'Oliy Majlis tomonidan yangi qonun loyihasi muhokama qilinmoqda. Ushbu qonun loyihasi fuqarolarning huquqlarini himoya qilish va davlat boshqaruvini takomillashtirishga qaratilgan. Ekspertlar bu qonunning ahamiyati haqida fikr bildirishmoqda.',
        'category': 'Siyosat',
        'tags': 'siyosat, qonun, majlis',
    },
    {
        'title': 'IT sohasida yangi ish orinlari',
        'slug': 'it-sohasida-yangi-ish',
        'body': 'Ozbekiston IT sohasida songgi yilda 15 mingdan ortiq yangi ish orinlari yaratildi. Dasturchilar, dizaynerlar va data tahlilchilariga bolgan talab ortib bormoqda. Bir qator xalqaro kompaniyalar ham Ozbekistonda oz ofislarini ochmoqda.',
        'category': 'Texnologiya',
        'tags': 'texnologiya, IT, ish',
    },
    {
        'title': 'Dehqonchilikda zamonaviy usullar',
        'slug': 'dehqonchilikda-zamonaviy-usullar',
        'body': 'Ozbekiston qishloq xojaligida zamonaviy texnologiyalarni qollash jadallashtirilmoqda. Dronlar, suniy intellekt va IoT qurilmalari orqali ekin maydonlarini boshqarish samaradorligi oshirilmoqda. Bu yangiliklar fermerlar uchun katta imkoniyatlar yaratmoqda.',
        'category': 'Iqtisodiyot',
        'tags': 'qishloq, texnologiya, dehqonchilik',
    },
]

for data in posts_data:
    cat = Category.objects.get(name=data['category'])
    post, created = Post.objects.get_or_create(
        slug=data['slug'],
        defaults={
            'title': data['title'],
            'body': data['body'],
            'author': admin_user,
            'category': cat,
            'tags': data['tags'],
            'status': 'published',
        }
    )
    if created:
        print(f'Post: {data["title"][:50]}')

print('Done! Seed data created.')
