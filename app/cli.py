import argparse
import sys
from typing import List

from .datastore import DataStore
from .reader import CSVReader
from .reports import ReportFactory
from .errors import AppError


def parse_args(argv: List[str]|None = None
               ) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate reports from CSV files")
    parser.add_argument("--files", 
                        nargs="+",
                        required=True, 
                        help="CSV files")
    parser.add_argument("--report", 
                        required=True,  
                        choices=['average-rating', 
                                 'max-rating', 
                                 'min-rating', 
                                 'median-rating',
                                'average-price', 
                                'max-price', 
                                'min-price', 
                                'median-price'], 
                        default='average-rating',
                        help="Тип отчета: 'average-rating', \
                                'max-rating', 'min-rating', \
                                'median-rating',")
    parser.add_argument("--precision", 
                        type=int, 
                        default=2, 
                        help="Decimal precision for averages")
    parser.add_argument("--top", 
                        type=int, 
                        default=None, 
                        help="Show top N entries (optional)")
    return parser.parse_args(argv)


def run(argv: List[str]|None = None) -> int:
    args = parse_args(argv)
    try:
        reader = CSVReader(args.files)
        datastore = DataStore()
        datastore.add_records(reader)
        extra = {}
        if args.precision is not None:
            extra["precision"] = args.precision
        if args.top is not None:
            extra["top"] = args.top
        report = ReportFactory.create(args.report,
                                      datastore,
                                      **extra)
        
        report.build()
        print(report.render())
        return 0
    except AppError as exc:
        print(f"Error {getattr(exc, 'code', '')} {exc}",
              file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"Unexpected error: {exc}"
              , file=sys.stderr)
        return 1