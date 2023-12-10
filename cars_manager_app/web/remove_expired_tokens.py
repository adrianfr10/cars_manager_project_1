import json
import time
import schedule
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path



@dataclass
class TokenManager:
    path: str = Path.cwd().absolute().joinpath(f'{"cars_manager_app/web/tokens.json"}')

    def remove_expired_tokens(self) -> None:

        with open(self.path, 'r+') as file:
            data = json.load(file)
            tokens = data.get('tokens', [])

            valid_tokens = [token for token in tokens if
                            datetime.strptime(token['date'], '%Y-%m-%d %H:%M') > datetime.now() - timedelta(days=30)]
            data['tokens'] = valid_tokens
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()

def start_and_schedule() -> None:
    manager = TokenManager()
    manager.remove_expired_tokens()

    schedule.every().week.do(manager.remove_expired_tokens)


start_and_schedule()

while True:
    schedule.run_pending()
    time.sleep(3600 * 24)
