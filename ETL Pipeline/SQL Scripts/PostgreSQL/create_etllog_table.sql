-- Table: etl.etlextractlog

-- DROP TABLE IF EXISTS etl.etlextractlog;

CREATE TABLE IF NOT EXISTS etl.etlextractlog
(
    extractlogid integer NOT NULL DEFAULT nextval('etl.etlextractlog_extractlogid_seq'::regclass),
    processlogid integer NOT NULL,
    tablename character varying(200) COLLATE pg_catalog."default" NOT NULL,
    extractrowcount integer NOT NULL DEFAULT 0,
    starttime timestamp without time zone NOT NULL,
    endtime timestamp without time zone,
    lastextractdatetime timestamp without time zone,
    success integer NOT NULL DEFAULT 0,
    status character(1) COLLATE pg_catalog."default" NOT NULL,
    errormessage character varying(500) COLLATE pg_catalog."default",
    CONSTRAINT etlextractlog_pkey PRIMARY KEY (extractlogid)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS etl.etlextractlog
    OWNER to postgres;

GRANT ALL ON TABLE etl.etlextractlog TO etl;

GRANT ALL ON TABLE etl.etlextractlog TO postgres;