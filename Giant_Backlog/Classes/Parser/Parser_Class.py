import argparse
import os
import json

class Parser:
    def create_arg_parser(self):
        parser = argparse.ArgumentParser(version='Giant Bomb CLI v1.0.0')
        
        parser.add_argument('-1', '--limit', dest='limit', action='store', type=int,
                            default=25, metavar='<x>', 
                            help='limits the amount of items requested, defaults to %(default)s')
        
        parser.add_argument('--offset', dest="offest", action="store", type=int,
                        default=0, metavar="<x>",
                        help="specify the offest into the results, defaults to %(default)s")

        parser.add_argument('--quality', dest="quality", action="store",
                            default="hd",
                            help="the quality of the video, used when streaming or downloading" +
                            " (low, high, hd) defaults to %(default)s")

        parser.add_argument('--output', dest="outputFolder", action="store",
                            help="the folder to output downloaded content to")
        
        parser.add_argument('--filter', dest='shouldFilter', action='store_true',
                            help='will attempt to filter by the below arguments', default=False)

        parser.add_argument('--sort', dest="sortOrder", action="store", default="desc",
                            help="orders the videos by their id (asc/desc) defaults to desc")
        
        # Filter options
        filter_opts = parser.add_argument_group("Filter options",
                                                "Use these in conjunction with " +
                                                "--filter to customise results")

        filter_opts.add_argument('--name', dest="filterName", action="store",
                                help="search for videos containing the specified phrase in the name")

        filter_opts.add_argument('--id', dest="contentID", action="store", help="id of the video")

        filter_opts.add_argument('--video_show', dest="videoShow", action="store",
                                help="id of the video show (see --dump_video_shows)")
        
        args = parser.parse_args()
        return args
        
    def validate_args(self, args, logger):
        # Validate filter arguments
        if args.shouldFilter is False:
            if args.filterName is not None or args.contentID is not None or args.videoShow is not None:
                logger.warning('Please use --filter command to process filter arguments')
                return False
            
        if args.quality != None:
            if args.quality not in ['low', 'high', 'hd']:
                logger.warning('Invalid quality value, options are \'low\', \'high\', \'hd\'')
                return False

        if args.sortOrder != "asc" or args.sortOrder != "desc":
            logger.warning('Invalid sort value, options are \'asc\' or \'desc\'')
            return False
        
    def get_api_key(self):
        # Change directory to path of file
        os.chdir(os.path.dirname(__file__))
        
        if os.path.exists('../../api.config') is False:
            os.makedirs('../../api.config')
        
        config_file_path = '../../api.config'
        
        config_json = json.loads('{}')
        if os.path.isfile(config_file_path):
            config_json = json.load(open(config_file_path, 'r'))
        else:
            user_api = input('Please enter your API key: ')
            config_json['api_key'] = user_api.strip()
            json.dump(config_json, open(config_file_path, 'w'))
        
        return config_json['api_key']