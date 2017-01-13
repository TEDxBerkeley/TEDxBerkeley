"""Read in JSON and spit out Swift data for a particular year.

Usage:
    dataToSwift.py (speakers|team|performers) <year>
    dataToSwift.py (speakers|team|performers) <year> <dir>
"""

import docopt
import json
import os
import shutil


PREFIX = '../../static/images/speakerPics/'


def convert(prefix: str, year: str, dest: str) -> None:
    """Converted provided year in JSON.

    Specifically, extracts all data for given year. Then, collects three pieces
    of information for every speaker, then outputting three lists:

        <prefix>Names
        <prefix>Bylines
        <prefix>Images

    """
    json_file = 'speakers.json' if prefix in ('speaker', 'performer') \
                else 'team.json'
    data = json.load(open(json_file))
    speakers_by_year = data[year]

    if prefix == 'speaker':
        speakers_by_year = [speaker for speaker in speakers_by_year
                            if speaker['byline'].lower() != 'performer']
    elif prefix == 'performer':
        speakers_by_year = [speaker for speaker in speakers_by_year
                            if speaker['byline'].lower() == 'performer']

    names = [speaker['name'] for speaker in speakers_by_year]
    bylines = [speaker['byline'] for speaker in speakers_by_year]
    image_uris = [os.path.basename(speaker['image_uri'])
                  for speaker in speakers_by_year]

    for image_uri in image_uris:
        path = os.path.join(PREFIX, image_uri)
        if os.path.exists(path):
            dst = os.path.join(dest, image_uri)
            open(dst, 'a').close()  # create the file if it doesn't exist
            shutil.copy(path, dst)

    stringify = lambda lst: str(lst).replace("'", '"')

    print('let %sNames =' % prefix, stringify(names))
    print('let %sBylines =' % prefix, stringify(bylines))
    print('let %sImageUris =' % prefix, stringify(image_uris))


def main() -> None:
    """Run convert method with command-line arguments."""

    arguments = docopt.docopt(__doc__)

    if arguments['speakers']:
        prefix = 'speaker'
    elif arguments['team']:
        prefix = 'team'
    else:
        prefix = 'performer'

    convert(
        prefix,
        arguments['<year>'],
        arguments['<dir>'] or '../../../../speakerPicsForiOS/')


if __name__ == '__main__':
    main()
