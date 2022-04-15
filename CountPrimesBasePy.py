
from timeit import default_timer;


class PrimeCounter:

    _size   :int
    _bits   :list

    VALID_PRIMES :dict = { 10 : 4,                                          # Historical Prime data upto 10**8
                          100 : 25,
                        1_000 : 168,
                       10_000 : 1_229,
                      100_000 : 9_592,
                    1_000_000 : 78_498,
                   10_000_000 : 664_579,
                  100_000_000 : 5_761_455 };



    def __init__( self, pool_size:int ) -> None:
        self._size = pool_size;
        self._bits = bytearray( b'\x01' ) *( ( self._size +1 )//2 );





    def countPrimes( self ) -> int:                                         # Add all elements of array
        return self._bits.count( b'\x01' )





    def runSieve( self ) -> None:                                           # Toggle all non-primes in _bit array

        START_VALUE = 3;                                                    # Number to start from
        INCREMENT   = 2;                                                    # Increments by 2 to skip even numbers
        MAX_LENGTH  = int( self._size **0.5 ) +1;                           # Prevents excess loop indicies

        for number in range( START_VALUE, MAX_LENGTH, INCREMENT ):
            if( self._bits[ number //2 ] ):                                 # Check bit
                bitlen = len( self._bits ) -( number *1.5 );                # Get the remaining length of the available array [ CURRENT -> END ]
                bitlen = int( bitlen /number ) +( number &1 );              # Devide by the index for the amount of remaining multiples and add (index==ODD)
                self._bits[ int( number *1.5 ) ::number ] =b'\x00' *bitlen; # Toggle bits*( amount of bits to change ) to b\x00 == ZERO





    def validatePrimes( self, count:int ) -> bool:                          # Confirm the number of found primes against known primes
        if( self._size in self.VALID_PRIMES ):
            return count == self.VALID_PRIMES[ self._size ];
        return False;





    def printf( self, ET:float, PASSES:int ) -> None:                       # Print the results of the sieve 
        count = self.countPrimes( )
        result = self.validatePrimes( count );
        if( not result ): print( 'RESULTS UNCONFIRMED' );
        print( f'PASSES:{PASSES}, ELAPSED TIME:{ET}, AVG:{ET/PASSES}, LIMIT:{self._size}, COUNT:{count}, Valid:{result}');





if __name__ == '__main__':
    ELAPSED_TIME = lambda START_TIME: default_timer( ) -START_TIME;
    START_TIME = default_timer( );          # <- Begin timer!!


    numer_of_passes :int = 0;
    while( ELAPSED_TIME( START_TIME ) < 5 ):
        PC = PrimeCounter( 1_000_000 );
        PC.runSieve( );
        numer_of_passes +=1;


    ET = ELAPSED_TIME( START_TIME );        # <- End timer!!
    PC.printf( ET, numer_of_passes );
