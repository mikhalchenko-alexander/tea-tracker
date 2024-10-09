import threading
import time

import flet as ft
import reactivex as rx
from reactivex import operators as ops

from scales.weights import empty, empty_teapot, full_teapot, full_teapot_cap, identify_teapot_state
from state.scale_state import scales_model


def format_seconds(seconds):
    sign = "-" if seconds < 0 else ""

    abs_seconds = abs(seconds)

    hours = abs_seconds // 3600
    minutes = (abs_seconds % 3600) // 60
    secs = abs_seconds % 60

    if hours > 0:
        return f"{sign}{hours:02}:{minutes:02}:{secs:02}"
    else:
        return f"{sign}{minutes:02}:{secs:02}"


def format_statistics(stats):
    session_timer, state, weight = stats
    weight = float(weight)
    v = [f"{session_timer:02} sec", f"{weight:.1f} gr.", f"{state}"]
    if 'water' in state:
        v.append(f"Left: {session_timer:02} sec")
    print(v)
    return ",\n".join(v)
    return str(stats)


def state2filename(state):
    str = 'empty' if state == {'empty'} else 'tea_cup'
    str += '+water' if 'water' in state else ''
    str += '+cap' if 'cap' in state else ''

    return str + '.png'


def create_countdown(countdown_timer, start_from=10):
    return countdown_timer.pipe(
        ops.scan(lambda acc, _: acc - 1, start_from),
    )


def emit_list(list, observer):
    def emit():
        observer.on_next(0.)
        delay = 0.1

        for func, count in list:
            for _ in range(int(count / delay)):
                observer.on_next(func())
                time.sleep(delay)

        observer.on_completed()

    threading.Thread(target=emit).start()


def none_to_full_stream(observer, scheduler):
    emit_list([
        (empty, 2),
        (empty_teapot, 1),
        (full_teapot, 3),
        (full_teapot_cap, 3),
    ], observer)


def to_none_stream(observer, scheduler):
    emit_list([
        (empty, 0)
    ], observer)


# def numbers_stream(observer, scheduler):

    # emit_list([
    #     (empty, 2),
    #     (empty_teapot, 1),
    #     (full_teapot, 3),
    #     (full_teapot_cap, 3),
    #     (empty_teapot, 2),
    #     (full_teapot, 18),
    #     (empty, 4),
    # ], observer)


def update_objects(page: ft.Page, objects: set[str]):
    if scales_model.set_objects(objects):
        page.update()


def update_weight(page: ft.Page, grams: float):
    if scales_model.set_weights(grams):
        page.update()


def simulate_scales(page: ft.Page):
    weight = rx.create(none_to_full_stream).pipe(ops.publish())

    state = weight.pipe(
        ops.map(lambda v: identify_teapot_state(v)),
        ops.distinct_until_changed(),
    )

    state.subscribe(
        lambda objects: update_objects(page, objects)
    )
    weight.subscribe(
        on_next = lambda grams: update_weight(page, grams),
        on_completed = lambda: print('end')
    )

    weight.connect()
