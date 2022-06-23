from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import mapper, sessionmaker


class AvitoDb:

    class RentRoom:
        def __init__(self, id, total_floors, title, phone, time, price, distance, metro, address, url):
            self.id = id
            self.total_floors = total_floors
            self.title = title
            self.phone = phone
            self.time = time
            self.price = price
            self.distance = distance
            self.metro = metro
            self.address = address
            self.url = url

    def __init__(self):
        self.new_room_count = 0
        # создаём движок бд:
        self.database_engine = create_engine('sqlite:///rooms.db3',
                                             echo=False, pool_recycle=7200,
                                             connect_args={
                                                 'check_same_thread': False
                                                 })
        # echo=False - отключает вывод на экран sql-запросов)
        # pool_recycle - по умолчанию соединение с БД через 8 часов простоя обрывается
        # Чтобы этого не случилось необходимо добавить pool_recycle=7200 (переустановка
        # соединения через каждые 2 часа)

        self.metadata = MetaData()
        ad = Table('Rooms', self.metadata,
                   Column('id', Integer, primary_key=True),  # имя колонки должно совпадать с полем класса
                   Column('total_floors', Integer),
                   Column('title', String),
                   Column('phone', String),
                   Column('time', DateTime),
                   Column('price', Integer),
                   Column('distance', Integer),
                   Column('metro', String),
                   Column('address', String),
                   Column('url', String),
                   )

        # создание таблицы:
        self.metadata.create_all(self.database_engine)

        # связываем данные и таблицы:
        mapper(self.RentRoom, ad)

        # создание сессии:
        Session = sessionmaker(bind=self.database_engine)
        self.session = Session()
        self.session.commit()

    def update_db(self, **kwargs):
        new_ad = self.session.query(self.RentRoom).filter_by(id=kwargs['id']).first()
        if not new_ad:
            new_ad = self.RentRoom(**kwargs)
            self.session.add(new_ad)
            self.session.commit()
            self.new_room_count += 1

    def get_all_id(self):
        """
        get all id from db
        and return list
        """
        all_id = []
        for i in self.session.query(self.RentRoom.id):
            all_id.extend(i)
        return all_id

    def get_from_db(self):
        ad = self.session.query(self.RentRoom).filter(self.RentRoom.total_floors > 5)
        return ad


if __name__ == '__main__':
    a = AvitoDb()
    # a.update_db()
