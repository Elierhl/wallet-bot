# URLS
CC_SEND_CRYPTO = 'https://new.cryptocurrencyapi.net/api/{currency}/.send'
CC_GIVE_ADDRESS = 'https://new.cryptocurrencyapi.net/api/{currency}/.give'
CG_GET_PRICE = 'https://api.coingecko.com/api/v3/simple/price'

# Phrases
NETWORKS = {
    'BTC': 'Bitcoin',
}

MAIN_MENU = {
    'start': 'Добро пожаловать в наш wallet-bot 👋',
    'menu': 'Это главное меню 🏠',
    'my_wallet': '💰 Это ваш кошелек\n\n'
    'Bitcoin: {btc} BTC {btc_rub_equivalent}\n\n'
    'USDT: {usdt} USDT {usdt_rub_equivalent}',
    'support': 'Здесь будет тех. поддержка.',
    'settings': 'Здесь будут настройки.',
    'rub_equivalent': ' ≈ {rub} RUB',
}

DEPOSIT = {
    'currency': 'Какую монету хотите внести?',
    'address': 'Пополнение: {currency}\n\n'
    'Используйте этот адрес для отправки {currency} на кошелек бота.\n'
    'Сеть: {network} - {currency}.\n\n'
    '{address}\n\n'
    'Средства будут зачислены в течение 30-60 минут.',
}

WITHDRAW = {
    'currency': 'Какую монету хотите перевести?',
    'address': 'На какой адрес отправить?',
    'wrong_address': 'Введен некорректный адрес. Адрес должен состоять из 34 символов (латинские буквы и цифры). '
    'Введите адрес повторно.',
    'amount': 'Какую сумму переводим?',
    'wrong_amount': 'Введена некорректная сумма. Попробуйте еще раз. Пример: 0.001',
    'confirmation': 'Перевод {amount} {currency} на адрес {address}.\nВсе верно?',
    'success': '✅ Транзакция на перевод средств создана. Ожидайте зачисления.',
    'failed': '❌ Что-то пошло не так. Проверьте все данные и повторите попытку позднее.',
}

BUTTONS = {
    'menu': '🏠 Открыть главное меню',
    'my_wallet': '💰 Мой кошелек',
    'support': '❓ Поддержка',
    'settings': '⚙️ Настройки',
    'back': '🔙 Назад',
    'back_to_main_menu': '🔙 Назад в главное меню',
    'deposit': '➕ Пополнить',
    'withdraw': '💸 Вывести',
    'transactions': '📄 Транзакции',
    'BTC': 'BTC',
    'yes_confirm': '✅ Да, все верно',
}


TRANSACTIONS = {
    'empty_transactions': 'У вас еще не было транзакций.',
}

UI_COMMANDS = {
    'start': '🤖 Стартовое сообщение',
    'menu': '🏠 Главное меню',
    'my_wallet': '💰 Мой кошелек',
}
