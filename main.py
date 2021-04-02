from configparser import ConfigParser

import os
import subprocess
import time

import psutil
from pypresence import Presence


DETAILS = {'KH1': 'Kingdom Hearts 1.5 💙', 'KHCoM': 'Chain of Memories 🤍',
           'KH358': '358/2 Days ❤', 'KH2': 'Kingdom Hearts 2 💜',
           'KHBbS': 'Birth by Sleep 🧡', 'KHC': 'Coded 💛',
           'KH3': 'Kingdom Hearts 3🖤'
           }
PROGRAM_NAME = {'KH1': 'KINGDOM HEARTS FINAL MIX.exe',
                'KHCoM': 'KINGDOM HEARTS Re_Chain of Memories.exe',
                'KH2': 'KINGDOM HEARTS II FINAL MIX.exe',
                'KHBbS': 'KINGDOM HEARTS Birth by Sleep FINAL MIX.exe',
                'KHL': 'KINGDOM HEARTS HD 1.5+2.5 Launcher.exe',
                'KHM': 'KINGDOM HEARTS HD 1.5+2.5 ReMIX.exe'
                }
IMAGES = {'KH1': 'kh', 'KHCoM': 'khcom', 'KH2': 'kh2', 'KHBbS': 'kh1_5_2_5',
          'KHL': 'kh1_5_2_5', 'KH12': 'kh1_5_2_5', 'KH3': 'kh3', 'KHH': 'khh'
          }
paths = {'KH12': f'{os.path.abspath(os.getcwd())}\KINGDOM HEARTS HD 1.5+2.5 ReMIX.exe',
         'KH3': f'{os.path.abspath(os.getcwd())}\KINGDOM HEARTS 3.exe'}

rpc = Presence(827398544986079242)

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)

if config['Program']['KH12']:
    paths['KH12'] = config['Program']['KH12']

if config['Program']['KH12']:
    paths['KH3'] = config['Program']['KH3']

state = "KINGDOM HEARTS 1.5 and 2.5 ReMIX" if config[
    'State']['KH12'] == '<True>' else "KINGDOM HEARTS 3"
print(f'State: {state}\n')

up_flag = 0
connect_flag = 0
game_flags = {'KH1': False, 'KHCoM': False, 'KH2': False, 'KHBbS': False,
              'KHL': False, 'KH12': False, 'KH3': False, 'KHH': False
              }

try:
    while True:
        subprocesses = subprocess.check_output('tasklist', shell=True)

        if not up_flag:
            try:
                if config['State']['KH12'] == '<True>':
                    os.startfile(paths['KH12'])
                elif config['State']['KH12'] == '<False>':
                    os.startfile(paths['KH3'])
                up_flag = 1
            except Exception as ex:
                print(ex)
                break

        # KHL
        if PROGRAM_NAME['KHL'] in (p.name() for p in psutil.process_iter()) and not connect_flag:
            print('LAUNCHER detected!')
            print('Connecting presence...')
            rpc.connect()
            print('Presence connected!\n')
            start = time.time()
            rpc.update(details='KH Main Menu | 358/2D | C', start=start,
                       large_image=IMAGES['KHL'], large_text='Main Menu | 358/2D | C')
            connect_flag = 1
            game_flags['KHL'] = True

        # Kingdom Hearts 1
        if PROGRAM_NAME['KH1'] in (p.name() for p in psutil.process_iter()) and not game_flags['KH1']:
            print('KH1 detected!')
            print('Updating presence...')
            start = time.time()
            rpc.update(details=DETAILS['KH1'], start=start,
                       large_image=IMAGES['KH1'], large_text='KH1',
                       small_image=IMAGES['KHH'], small_text='Kingdom Hearts❣')
            print('Presence updated!\n')
            game_flags['KH1'] = True

        # Kingdom Hearts Chain of Memories
        if PROGRAM_NAME['KHCoM'] in (p.name() for p in psutil.process_iter()) and not game_flags['KHCoM']:
            print('KHCoM detected!')
            print('Updating presence...')
            start = time.time()
            rpc.update(details=DETAILS['KHCoM'], start=start,
                       large_image=IMAGES['KHCoM'], large_text='KHCoM',
                       small_image=IMAGES['KHH'], small_text='Kingdom Hearts❣')
            print('Presence updated!\n')
            game_flags['KHCoM'] = True

        # Kingdom Hearts 2
        if PROGRAM_NAME['KH2'] in (p.name() for p in psutil.process_iter()) and not game_flags['KH2']:
            print('KH2 detected!')
            print('Updating presence...')
            start = time.time()
            rpc.update(details=DETAILS['KH2'], start=start,
                       large_image=IMAGES['KH2'], large_text='KH2',
                       small_image=IMAGES['KHH'], small_text='Kingdom Hearts❣')
            print('Presence updated!\n')
            game_flags['KH2'] = True

        # Kingdom Hearts Birth by Sleep
        if PROGRAM_NAME['KHBbS'] in (p.name() for p in psutil.process_iter()) and not game_flags['KHBbS']:
            print('KHBbS detected!')
            print('Updating presence...')
            start = time.time()
            rpc.update(details=DETAILS['KHBbS'], start=start,
                       large_image=IMAGES['KHBbS'], large_text='KHBbS',
                       small_image=IMAGES['KHH'], small_text='Kingdom Hearts❣')
            print('Presence updated!\n')
            game_flags['KHBbS'] = True

        # Kingdom Hearts 1
        if PROGRAM_NAME['KH1'] not in (p.name() for p in psutil.process_iter()) and game_flags['KH1']:
            print('KH1 not detected anymore')
            print('Checking if main game is running...\n')
            time.sleep(10)

            if PROGRAM_NAME['KHM'] not in (p.name() for p in psutil.process_iter()):
                print('The game is not running...\n')
                if connect_flag:
                    rpc.close()
                print('Disconnecting presence')
                print('Exiting program...')
                time.sleep(2)
                break
            else:
                print('The game is still running!')
                print('Checking if Launcher is running...\n')
                time.sleep(5)

                if PROGRAM_NAME['KHL'] in (p.name() for p in psutil.process_iter()):
                    print('Launcher is running!')
                    print('Updating presence...')
                    start = time.time()
                    rpc.update(details='KH Main Menu | 358/2D | C', start=start,
                               large_image=IMAGES['KHL'], large_text='Main Menu | 358/2D | C')
                    print('Presence updated!\n')
                    game_flags['KHL'] = True
                else:
                    print('Launcher is no longer running')
                    print('Assuming game\'s no longer running')
                    if connect_flag:
                        rpc.close()
                    print('Disconnecting presence')
                    print('Exiting program...')
                    time.sleep(2)
                    break

            game_flags['KH1'] = False

        # Kingdom Hearts Chain of Memories
        if PROGRAM_NAME['KHCoM'] not in (p.name() for p in psutil.process_iter()) and game_flags['KHCoM']:
            print('KHCoM not detected anymore')
            print('Checking if main game is running...\n')
            time.sleep(10)

            if PROGRAM_NAME['KHM'] not in (p.name() for p in psutil.process_iter()):
                print('The game is not running...\n')
                if connect_flag:
                    rpc.close()
                print('Disconnecting presence')
                print('Exiting program...')
                time.sleep(2)
                break
            else:
                print('The game is still running!')
                print('Checking if Launcher is running...\n')
                time.sleep(5)

                if PROGRAM_NAME['KHL'] in (p.name() for p in psutil.process_iter()):
                    print('Launcher is running!')
                    print('Updating presence...')
                    start = time.time()
                    rpc.update(details='KH Main Menu | 358/2D | C', start=start,
                               large_image=IMAGES['KHL'], large_text='Main Menu | 358/2D | C')
                    print('Presence updated!\n')
                    game_flags['KHL'] = True
                else:
                    print('Launcher is no longer running')
                    print('Assuming game\'s no longer running')
                    if connect_flag:
                        rpc.close()
                    print('Disconnecting presence')
                    print('Exiting program...')
                    time.sleep(2)
                    break

            game_flags['KHCoM'] = False

        # Kingdom Hearts 2
        if PROGRAM_NAME['KH2'] not in (p.name() for p in psutil.process_iter()) and game_flags['KH2']:
            print('KH2 not detected anymore')
            print('Checking if main game is running...\n')
            time.sleep(10)

            if PROGRAM_NAME['KHM'] not in (p.name() for p in psutil.process_iter()):
                print('The game is not running...\n')
                if connect_flag:
                    rpc.close()
                print('Disconnecting presence')
                print('Exiting program...')
                time.sleep(2)
                break
            else:
                print('The game is still running!')
                print('Checking if Launcher is running...\n')
                time.sleep(5)

                if PROGRAM_NAME['KHL'] in (p.name() for p in psutil.process_iter()):
                    print('Launcher is running!')
                    print('Updating presence...')
                    start = time.time()
                    rpc.update(details='KH Main Menu | 358/2D | C', start=start,
                               large_image=IMAGES['KHL'], large_text='Main Menu | 358/2D | C')
                    print('Presence updated!\n')
                    game_flags['KHL'] = True
                else:
                    print('Launcher is no longer running')
                    print('Assuming game\'s no longer running')
                    if connect_flag:
                        rpc.close()
                    print('Disconnecting presence')
                    print('Exiting program...')
                    time.sleep(2)
                    break

            game_flags['KH2'] = False

        # Kingdom Hearts Birth by Sleep
        if PROGRAM_NAME['KHBbS'] not in (p.name() for p in psutil.process_iter()) and game_flags['KHBbS']:
            print('KHBbS not detected anymore')
            print('Checking if main game is running...\n')
            time.sleep(10)

            if PROGRAM_NAME['KHM'] not in (p.name() for p in psutil.process_iter()):
                print('The game is not running...\n')
                if connect_flag:
                    rpc.close()
                print('Disconnecting presence')
                print('Exiting program...')
                time.sleep(2)
                break
            else:
                print('The game is still running!')
                print('Checking if Launcher is running...\n')
                time.sleep(5)

                if PROGRAM_NAME['KHL'] in (p.name() for p in psutil.process_iter()):
                    print('Launcher is running!')
                    print('Updating presence...')
                    start = time.time()
                    rpc.update(details='KH Main Menu | 358/2D | C', start=start,
                               large_image=IMAGES['KHL'], large_text='Main Menu | 358/2D | C')
                    print('Presence updated!\n')
                    game_flags['KHL'] = True
                else:
                    print('Launcher is no longer running')
                    print('Assuming game\'s no longer running')
                    if connect_flag:
                        rpc.close()
                    print('Disconnecting presence')
                    print('Exiting program...')
                    time.sleep(2)
                    break

            game_flags['KHBbS'] = False

            # Kingdom Hearts Launcher
        if PROGRAM_NAME['KHL'] not in (p.name() for p in psutil.process_iter()) and game_flags['KHL'] and PROGRAM_NAME['KHM'] not in (p.name() for p in psutil.process_iter()):
            print('Launcher and main game not detected anymore')

            if connect_flag:
                rpc.close()

            print('Disconnecting presence')
            print('Exiting program...')
            time.sleep(2)
            break

        time.sleep(1)

except KeyboardInterrupt:
    if connect_flag:
        rpc.close()
    print('Disconnecting presence...')
    print('Exiting program...')
    time.sleep(2)
