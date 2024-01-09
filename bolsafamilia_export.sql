---
START TRANSACTION;
CREATE TABLE Saques (
        AnoMesReferencia TEXT,
        AnoMesCompetencia TEXT,
        UF TEXT,
        CodigoMunicipioSIAFI INTEGER,
        NomeMunicipioSIAFI TEXT,
        CPFBeneficiario TEXT,
        NISBeneficiario TEXT,
        NomeBeneficiario TEXT,
        DataSaque DATE,
        ValorParcela DECIMAL
    );
CREATE TABLE Pagamentos (
        AnoMesReferencia TEXT,
        AnoMesCompetencia TEXT,
        UF TEXT,
        CodigoMunicipioSIAFI INTEGER,
        NomeMunicipioSIAFI TEXT,
        CPFBeneficiario TEXT,
        NISBeneficiario TEXT,
        NomeBeneficiario TEXT,
        ValorParcela DECIMAL
    );
COMMIT;
