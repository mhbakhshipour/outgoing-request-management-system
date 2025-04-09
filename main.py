import uuid
import time
import heapq
import asyncio
from datetime import datetime

from typing import Any, Dict


class Provider:
    def __init__(self, name: str, rate_limit: float):
        self.name = name
        self.rate_limit = rate_limit
        self.next_available_time = 0.0
        self.queue = []

    async def process_requests(self) -> None:
        while True:
            if self.queue:
                priority, correlation_id, data = heapq.heappop(self.queue)
                remaining_next_available_time = self.next_available_time - time.time()

                if remaining_next_available_time > 0.0:
                    await asyncio.sleep(remaining_next_available_time)
                self.next_available_time = time.time() + (1 / self.rate_limit)
                print(
                    f"[{datetime.now()}] Processed Request {correlation_id} for {self.name} (Priority {priority}) - (Data {data})"
                )
            else:
                break

    def add_request(
        self, correlation_id: uuid, priority: int, data: Dict[str, Any]
    ) -> None:
        heapq.heappush(self.queue, (priority, correlation_id, data))


async def main() -> None:
    providers = {
        "NOBITEX": Provider("NOBITEX", rate_limit=0.2),
        "SHAPARAK": Provider("SHAPARAK", rate_limit=0.1),
    }

    for provider in providers.values():
        asyncio.create_task(provider.process_requests())

    providers["NOBITEX"].add_request(
        correlation_id=uuid.uuid4(), priority=2, data={"payload": "data1"}
    )
    providers["SHAPARAK"].add_request(
        correlation_id=uuid.uuid4(), priority=1, data={"payload": "data2"}
    )
    providers["NOBITEX"].add_request(
        correlation_id=uuid.uuid4(), priority=1, data={"payload": "data3"}
    )
    providers["SHAPARAK"].add_request(
        correlation_id=uuid.uuid4(), priority=3, data={"payload": "data4"}
    )

    await asyncio.sleep(15)


if __name__ == "__main__":
    asyncio.run(main())
