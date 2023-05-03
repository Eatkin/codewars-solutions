-- /kata/57eae65a4321032ce000002d
SELECT x, REPLACE(
  REPLACE(
    REPLACE(
      REPLACE(
        REPLACE(
          REPLACE(
            REPLACE(
              REPLACE(
                REPLACE(x, '1', '0')
                , '2', '0')
              , '3', '0')
            , '4', '0')
          , '5', '1')
        , '6', '1')
      , '7', '1')
    , '8', '1')
  , '9', '1')
as res FROM fakebin;