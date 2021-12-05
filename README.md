# Fast API

## Install

```bash
pip install -r requirements.txt
```

<br>

## Run Server

```bash
uvicorn main:app --reload
```

<br>

## Fast API 장점

- 비동기식이기 때문에 I/O 병목이 대부분인 웹 서버에서 빠른 성능을 보여준다.
- 빠르다.
- 구조가 단순해 생산성이 좋다.
- 타입 힌트를 강제하는 면이 있어 버그를 적게 유발한다(휴먼에러를 피할 수 있음).
- 기본적으로 쉽게 디자인됐기 때문에 문서도 방대하지 않다.
- API문서를 자동으로 만들어준다.


<br>

## References

- [Building a Website Starter with FastAPI](https://levelup.gitconnected.com/building-a-website-starter-with-fastapi-92d077092864)