FROM ruby:2.3

# Set the locale - this is so UTF-8 is handled correctly
ENV LANG C.UTF-8

# Create a directory for the site to go in and expose it
RUN ["mkdir", "/site"]
VOLUME /site

# Copy the gemfile
COPY Gemfile /Gemfile

# Install the package manager
RUN ["gem", "install", "bundler"]

# Install all our dependencies
RUN ["bundle", "install"]

# From now on commands will be run from this dir
WORKDIR /site

# Expose the port jekyll will serve the site through
EXPOSE 4000

# If no command given, just serve the site
CMD ["jekyll", "serve", "--host", "0.0.0.0"]
