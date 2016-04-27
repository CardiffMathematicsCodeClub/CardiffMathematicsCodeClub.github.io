FROM ruby:2.3

# Create a directory for the site to go in and expose it
RUN ["mkdir", "/site"]
VOLUME /site

# Copy the gemfile
COPY Gemfile /Gemfile

# Install all our dependencies
RUN ["bundle", "install"]

# From now on commands will be run from this dir
WORKDIR /site

# Expose the port jekyll will serve the site through
EXPOSE 4000

# If no command given, just serve the site
CMD ["jekyll", "serve", "--host", "0.0.0.0"]
